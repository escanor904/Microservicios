from flask import Flask, request, jsonify
import psycopg2,  jsonschema, json, sys
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from random import choices
from string import ascii_letters, digits
from datetime import datetime, timedelta
from config import db_config , DevelopmentConfig
from kafka import KafkaProducer

# Configura el productor Kafka
producer = KafkaProducer(
    # El nombre del servicio Kafka 
    bootstrap_servers='localhost:29092',  
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
        # Cargar el JSON Schema
        ruta_absoluta = "/home/escanor/Documentos/uniquindio-2023-2/Microservicios/taller_apirest_salome_version/schems/inicio_sesion_schema.json"
        ruta_relativa= "../taller_apirest_salome_version/schems/inicio_sesion_schema.json"     
        with open(ruta_relativa, 'r') as schema_file:
          schema = json.load(schema_file)
        # obtiene el JSON de respuesta
        api_response=request.get_json()

        # valida la respuesta
        jsonschema.validate(schema,api_response)
       
        
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
           mensaje = {"usuario": email, "accion": "inicio_sesion"}
           producer.send('autenticacion_log', value=mensaje)

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