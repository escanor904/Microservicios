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
def obtener_usuario(context,user_id):
    # Ejecuta una consulta SELECT para recuperar los datos del usuario según el user_id especificado       
    cursor = context.cursor_conect
    conn = context.conn_conect
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (context.user_id,))
    user = cursor.fetchone()
    # Cierra el cursor y la conexión con la base de datos.
    cursor.close()
    conn.close()
    context.user_data = user
    assert context.user!=None
    assert context.user_data!=None

@given('obtener la informacion del usuario no existente')
def establecer_conexion(context):  
    context.user = None
    context.user_data = None
    # Aseguro el usuario es diferente de null
    assert context.user==None
    assert context.user_data==None

@when('se verifica el id')
def usuario_existente(context,user_id):
    user = context.user_data
    if user:
        # Extrae los datos del usuario y crea una respuesta JSON
        user_data = {
            "id": user[0],
            "username": user[1],
            "email": user[3]
        }
        context.data_user = user_data
        assert context.data_user!=None
        pass
    else:
        mensaje = "El usuario no existe"
        context.mensaje_fallo = mensaje
        assert context.mensaje_falo != None
        pass

@then('mostrar la informacion del usuario')
def mostrar_usuario(context):
    #Mostramos la informacion del usuario
    user_data = context.data_user
    return jsonify(user_data), 200

@then('mostrar el mensaje de "Usuario no valido"')
def usuario_invalido(context):
    #Mostramos el mensaje de usuario no valido
    mensaje = context.mensaje_fallo
    return jsonify({"message": mensaje}), 404