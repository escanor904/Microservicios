
from flask import Flask, request, jsonify
import psycopg2, json
from flask_jwt_extended import JWTManager, create_access_token
from datetime import datetime
from config_productor import db_config , DevelopmentConfig, confluent_config
from confluent_kafka import Producer

producer = Producer(confluent_config)

app = Flask(__name__)
# Configuración del JWT
app.config['JWT_SECRET_KEY'] = DevelopmentConfig.SECRET_KEY
jwt = JWTManager(app)

# Almacén temporal para guardar los tokens de recuperación
#reset_tokens = {}


#--------------------------------------LOGIN-------------------------------------
@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():     
    try:
        # Establecer una conexión con la base de datos PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Obtener los datos del inicio de sesión desde la carga JSON de la solicitud HTTP
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        # Buscar al usuario en la base de datos por su email
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        
        if user and user[2] == password:  # Verificar contraseña (esto debe ser un hash en la vida real)
           # Generar un token JWT
           access_token = create_access_token(identity=email)
           
           # Autenticación exitosa, envía un mensaje a Kafka
           mensaje = {"event_type": "inicio_sesion", "user_email": email, "timestamp": str(datetime.now())}
           producer.produce('autenticacion-topic', key="key", value= convertirEnBytes(mensaje), callback=delivery_report)           # Cerrar el cursor y la conexión
           cursor.close()
           conn.close()

           return jsonify({"Token de acceso": access_token}), 200
        else:
           # Cerrar el cursor y la conexión
           cursor.close()
           conn.close()

        return jsonify({"mensaje": "Credenciales invalidas"}), 401
        
    #except jsonschema.exceptions.ValidationError as e:
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
    app.run()