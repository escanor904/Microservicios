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

@given('establecer la conexion RC')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    # Aseguro que la coneccion es diferente de null
    assert conn != None
    



@given('establecer la conexion RC')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    # Aseguro que la coneccion es diferente de null
    assert conn != None
    
@when('El correo electronico que proporciona el usuario es "{email}"')
def obtener_email(context,email):  
    context.email=email
    assert email != None
    
@when('Buscar al usuario en la base de datos por su email RC')
def buscar_usuario_por_email(context):
     
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (context.email,))
    user = cursor.fetchone()
    context.user = user
    assert user != None
    
@when('Generar un token de recuperación de contraseña')    
def generar_token(context):
    # Datos a incluir en el token (en este caso, solo la dirección de correo electrónico)
    email = context.email
    
    # Crear el token JWT
    token = jwt.encode({"email": email}, "mypass", algorithm="HS256")
    context.token=token
    assert token!=None
    
@then('se muestra el token')
def enviar_reporte(context):
    assert context.token!= None
    
   
    


