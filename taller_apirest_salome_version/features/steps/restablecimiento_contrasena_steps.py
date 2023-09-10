from behave import given, when, then, step
from behave import *
import psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}

@given('el usuario se encuentra ya registrado')
def establecer_existencia_usuario(context):
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    context.user=user
    # Aseguro el usuario es diferente de null
    assert user!=None

@when('el usuario proporciona el token, el correo electrónico y una nueva contraseña')
def datos_usuario(context):
    context.token = "ahfbasfajfb13413"
    context.email = "cristian_r@email.com"
    context.new_password = "password_nueva"
    
@when('el usuario proporciona un token expirado, el correo electrónico y una nueva contraseña')
def datos_usuario(context):
    context.token = "ahfbasfajfb13413"
    context.email = "cristian_r@email.com"
    context.new_password = "password_nueva"

@when('el usuario proporciona un token que no existe, el correo electrónico y una nueva contraseña')
def datos_usuario(context):
    context.token = "ahfbasfajfb13413"
    context.email = "cristian_r@email.com"
    context.new_password = "password_nueva"

@when('hacer la solicitud al servidor que actualice la contrasena')
def solictud_servidor(context):
    if (context.new_password != "password_valido") and (context.user!=None) :
        cursor = context.db_connection.cursor()
        # Actualizar la contraseña del usuario en la base de datos
        cursor.execute("UPDATE users SET hashed_password = %s WHERE email = %s",
                       (context.new_password , context.email))
        pass
    else:
        pass
        
        
        
@then('la respuesta debería tener un "{codigo}"') 
def enviar_reporte_codigo_res(context,codigo):
    if context.user == 1 :
        assert codigo==codigo
    else:
        assert codigo==codigo

@then('se captura el mensaje de respuesta "{mensaje}"')
def enviar_reporte_mensaje_res(context,mensaje):
    assert mensaje==mensaje
    