from flask import Flask, request, jsonify
import psycopg2, json,  logging, jsonschema, requests, time
from flask_jwt_extended import JWTManager, create_access_token
from datetime import datetime
from config_productor import db_config , ProducerConfig
from kafka import KafkaProducer
#from confluent_kafka import Producer

#config = {
#    'bootstrap.servers': f'{ProducerConfig.KAFKA_SERVER}:{ProducerConfig.KAFKA_PORT}',  # Dirección del servidor Kafka
#    'client.id':  socket.gethostname()
#}

#producer= Producer(config)
producer = KafkaProducer(
    bootstrap_servers=[f'{ProducerConfig.KAFKA_SERVER}:{ProducerConfig.KAFKA_PORT}'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


app = Flask(__name__)
# Configuración del JWT
app.config['JWT_SECRET_KEY'] = ProducerConfig.SECRET_KEY
jwt = JWTManager(app)

# Almacén temporal para guardar los tokens de recuperación
#reset_tokens = {}

# Nombre del contenedor del servicio de logs
logs_container_name = "logsapp-cont"

#--------------------------------------LOGIN-------------------------------------
@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():     
    try:
        # Obtener los datos del inicio de sesión desde la carga JSON de la solicitud HTTP
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        # Establecer una conexión con la base de datos PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Buscar al usuario en la base de datos por su email
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and user[2] == password:  # Verificar contraseña (esto debe ser un hash en la vida real)
           # Generar un token JWT
           access_token = create_access_token(identity=email)
           # Cerrar el cursor y la conexión
           cursor.close()
           conn.close()
           
           # Autenticación exitosa, envía un mensaje a Kafka
           mensaje = {"nombre_app": "api_users", "log_type": "info", "descripcion": "inicio de sesión exitoso"}
           producer.send(ProducerConfig.KAFKA_TOPIC_NAME, value=mensaje)

           #crea un log para mostrar en consola 
           logging.basicConfig(level=logging.INFO,  # Establece el nivel de registro (puedes usar 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Define el formato del mensaje de registro
           logger = logging.getLogger(__name__)
           # Registra un mensaje
           logger.info('Mensaje enviado al tema: %s', ProducerConfig.KAFKA_TOPIC_NAME)  
 
        
           return jsonify({"Token de acceso": access_token}), 200
           
        else:
            # Cerrar el cursor y la conexión
            mensaje = {"nombre_app": "api_users", "log_type": "alert", "descripcion": "credenciales incorrectas"}
            producer.send(ProducerConfig.KAFKA_TOPIC_NAME, value=mensaje)

            cursor.close()
            conn.close()
            
            return jsonify({'message': 'Credenciales incorrectas'}), 401
    except Exception as e:
        
            mensaje = {"nombre_app": "api_users", "log_type": "error", "descripcion": "se produjo un error inesperado"}
            producer.send(ProducerConfig.KAFKA_TOPIC_NAME, value=mensaje)

            return jsonify({"mensaje": "Se produjo un error inesperado: " + str(e)}), 500

    except jsonschema.exceptions.ValidationError as e:
            return jsonify({"mensaje": "La respuesta no cumple con el JSON Schema: " + str(e)}), 400
 
    
#--------------------------------------CRUD--------------------------------------
# Definición de una ruta para el registro de usuarios
@app.route('/users', methods=['POST'])
def registro_usuario():
    # Establecer una conexión con la base de datos PostgreSQL
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Obtener los datos del usuario desde la carga JSON de la solicitud HTTP
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Verificar si alguno de los campos está vacío
        if not username or not password or not email:
            return jsonify({"error": "Diligencia todos los campos"}), 400

        # Verificar si el usuario ya existe (por nombre de usuario o correo electrónico)
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s OR email = %s", (username, email))
        existe_usuario = cursor.fetchone()[0]
        if existe_usuario:
            return jsonify({"error": "Ese usuario o corre electronico ya esta registrado"}), 409

        # Ejecutar una consulta SQL para insertar los datos del usuario en la tabla 'users'
        cursor.execute("INSERT INTO users (username, hashed_password, email) VALUES (%s, %s, %s)",
                       (username, password, email))

        # Confirmar la transacción y cerrar el cursor y la conexión
        conn.commit()
        cursor.close()
        conn.close()
        
    

        #se envia los datos del ususario para registrarlo en api managment
        mensaje = {"username":username, "user_email": email , "timestamp": str(datetime.now())}
        producer.send(ProducerConfig.KAFKA_TOPIC_MANAGMENT, value=mensaje)
        
        logging.basicConfig(level=logging.INFO,  # Establece el nivel de registro (puedes usar 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Define el formato del mensaje de registro
        logger = logging.getLogger(__name__)

        # Registra un mensaje
        logger.info('Mensaje enviado al tema: %s', ProducerConfig.KAFKA_TOPIC_MANAGMENT)  

        mensaje = {"event_type": "inicio_sesion", "user_email": email, "timestamp": str(datetime.now())}
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": "Error en el servidor"}), 500    
        
@app.route('/consultar_logs/<string:usuario>', methods=['GET'])
def consultar_logs(usuario):
    try:
        # Establecer una conexión con la base de datos PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Consultar los registros de logs para el usuario especificado
        cursor.execute("SELECT * FROM logs WHERE user_email = %s", (usuario,))
        logs = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        if logs:
            # Si se encontraron registros de logs para el usuario, devolverlos como JSON
            logs_data = [{"log_id": log[0], "evento": log[1], "user_email": log[2], "fecha_log": log[3]} for log in logs]
            return jsonify({"logs": logs_data}), 200
        else:
            return jsonify({"mensaje": "No se encontraron registros de logs para el usuario"}), 404

    except Exception as e:
        mensaje_de_error = str(e)
        return mensaje_de_error



def convertirEnBytes(diccionario):
    mensaje_json = json.dumps(diccionario)
    # Codificar la cadena JSON en bytes (utf-8 es una codificación común)
    mensaje_bytes = mensaje_json.encode('utf-8')
    return mensaje_bytes
            
           
def delivery_report(err, msg):
    if err is not None:
        print('Error al enviar el mensaje: {}'.format(err))
    else:
        print('Mensaje enviado a {} [{}]'.format(msg.topic(), msg.partition()))
           
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    #Se activa el debug para poder hacer cambios en el servidor en tiempo real
    app.debug = True
    app.register_error_handler(404, status_404)
    app.run(host='0.0.0.0', port=5000)