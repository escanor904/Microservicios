from flask import Flask, request, jsonify
import psycopg2
import jsonschema
import json
import sys
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from random import choices
from string import ascii_letters, digits
from datetime import datetime, timedelta
from config import db_config, DevelopmentConfig
import requests
import time

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = DevelopmentConfig.SECRET_KEY
jwt = JWTManager(app)

reset_tokens = []

# Nombre del contenedor del servicio de logs
logs_container_name = "logsapp-cont"

# Ruta para el inicio de sesión con parámetros en la URL
@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    try:
        # Obtener los datos del inicio de sesión desde la carga JSON de la solicitud HTTP
        data = request.get_json()
        email = data['email']
        password = data['password']
        nombre_app =  data['application']       
        tipo_log = data['log_type']             
        fecha_log = data['timestamp']           
        descripcion = data['description']       
        user_email = data['email']
       
    
        # Establecer una conexión con la base de datos PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Buscar al usuario en la base de datos por su email
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and user[2] == password:  # Verificar contraseña 
            # Generar un token JWT
            access_token = create_access_token(identity=email)
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # Datos para crear un registro de log
            log_data = {
                "application": nombre_app,
                "log_type": tipo_log,
                "timestamp": now,
                "description": descripcion,
                "email" : email
            }

            # Realizar una solicitud HTTP POST al servicio de logs para crear el registro
            logs_url = f"http://{logs_container_name}:8081/logs"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(logs_url, json=log_data, headers=headers)

            if response.status_code == 201:
                # Generar un token JWT y enviarlo como respuesta
                return jsonify({"Token de acceso": access_token}), 200
            else:
                return jsonify({'message': 'Error al crear el registro de log'}), 500
        else:
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            return jsonify({'message': 'Credenciales incorrectas'}), 401
    except Exception as e:
        return jsonify({"mensaje": "Se produjo un error inesperado: " + str(e)}), 500

    except jsonschema.exceptions.ValidationError as e:
        return jsonify({"mensaje": "La respuesta no cumple con el JSON Schema: " + str(e)}), 400

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    # Se activa el debug para poder hacer cambios en el servidor en tiempo real
    app.debug = True
    app.register_error_handler(404, status_404)
    app.run(host='0.0.0.0', port=5000)
