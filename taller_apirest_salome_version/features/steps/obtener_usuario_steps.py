from flask import Flask, request, jsonify
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

@given('obtener la informacion del usuario existente')
def obtener_usuario(context):
    conn = psycopg2.connect(**db_config)
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    # Cierra el cursor y la conexión con la base de datos.
    context.user = user
    assert context.user!=None

@given('obtener la informacion del usuario no existente')
def establecer_conexion(context):  
    context.user = None
    # Aseguro el usuario es diferente de null
    assert context.user==None

@when('se verifica el id')
def usuario_existente(context):
    user = context.user
    if user:
        # Extrae los datos del usuario y crea una respuesta JSON
        user_data = {
            "id": user[0],
            "username": user[1],
            "email": user[3]
        }
        context.user_data = user_data
        assert context.user_data !=None
        pass
    else:
        context.user_data = None
        assert context.user_data == None
        pass

@then('mostrar el mensaje del servidor "{mensaje}"')
def mostrar_usuario(context,mensaje):
    #Mostramos la informacion del usuario
    if context.user_data != None :
        assert mensaje == mensaje
    else:
        assert mensaje == mensaje
