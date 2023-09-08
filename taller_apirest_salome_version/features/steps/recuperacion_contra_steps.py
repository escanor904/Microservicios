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

@given('ser un usuario previamente registrado')
def tener_usuario_registrado(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    context.email="cristiano_r@email.com"
    cursor.execute("SELECT * FROM users WHERE email = %s", (context.email,))
    user = cursor.fetchone()
    context.user=user

    # Aseguro que la coneccion es diferente de null
    assert user!=None
    
@given('tener un usuario que no este registrado')
def tener_usuario_registrado(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    context.email="cristiano_@email.com"
    cursor.execute("SELECT * FROM users WHERE email = %s", (context.email,))
    user = cursor.fetchone()
    context.user=user
    # Aseguro que la coneccion es diferente de null
    assert user==None
    

@when('se realiza la solicitud al servidor')    
def generar_token(context):
    # Datos a incluir en el token (en este caso, solo la dirección de correo electrónico)
    email = context.email
    if email!=None :
            # Crear el token JWT
        token = jwt.encode({"email": email}, "mypass", algorithm="HS256")
        context.token=token
        assert token!=None
        
    else:
        assert token==None
    


@then('se obtiene el mensaje de respuesta "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.email!=None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje


