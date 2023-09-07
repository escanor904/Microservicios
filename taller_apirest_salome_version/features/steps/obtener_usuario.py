from behave import given, when, then, step
from flask_jwt_extended import get_jwt_identity
import psycopg2
import jwt

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}

@given('establecer la conexion')
def seleccionar_usuario(context):
    #Establecer la conexion con la base de datos
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

@given('obtener la informacion del usuario desde su id: "{user_id}')
def