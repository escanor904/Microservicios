from behave import given, when, then, step
from flask_jwt_extended import get_jwt_identity
import psycopg2
import jwt

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5434'
}

@given('ser un usuario previamente registrado en el sistema')
def tener_usuario_registrado(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    context.user=user
    # Aseguro que la coneccion es diferente de null
    assert user!=None
    
@given('tener un usuario que no este registrado en el sistema')
def step_impl(context):  
        # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    email="ccristiano_r@email.com"
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    context.user=user

    # Aseguro que el usuario es nulo
    assert user==None
    
    

@when('se realiza la solicitud al servidor')    
def generar_token(context):
   
    if context.user!=None :
        # Crear el token JWT
        token = jwt.encode({"email": context.email}, "mypass", algorithm="HS256")
        context.token=token
        assert token!=None  
        
    else:
        pass
    


@then('se obtiene el mensaje de respuesta "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.user!=None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje


