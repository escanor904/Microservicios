from flask import Flask, request, jsonify
import psycopg2,  jsonschema, json, sys
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from datetime import datetime
from config import db_config , DevelopmentConfig
from kafka import KafkaProducer

# Configura el productor Kafka
producer = KafkaProducer(
    # El nombre del servicio Kafka 
    bootstrap_servers='localhost:29092',
    # bootstrap_servers= 'kafka:29092',  #contenedor  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializa mensajes como JSON
)

app = Flask(__name__)
# Configuración del JWT
app.config['JWT_SECRET_KEY'] = DevelopmentConfig.SECRET_KEY
jwt = JWTManager(app)

# Almacén temporal para guardar los tokens de recuperación
reset_tokens = {}


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
           producer.send('autenticacion-topic', value=mensaje)

           # Cerrar el cursor y la conexión
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
        return jsonify({"mensaje": "La respuesta no cumple con el JSON Schema:"}), 400
        #print("La respuesta no cumple con el JSON Schema:")
        #print(e)
           
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    #Se activa el debug para poder hacer cambios en el servidor en tiempo real
    app.debug = True
    app.register_error_handler(404, status_404)
    app.run()