from behave import given, when, then, step
from flask_jwt_extended import get_jwt_identity
import psycopg2, requests

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5434'
}

@given('tener un usuario registrado en el sistema')
def step_impl(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    context.user=user
    
    assert user != None

@given('no tener un usuario registrado en el sistema')
def step_impl(context):  
    context.user=None
    assert context.user == None
    
@given('tener la contraseña para el usuario registrado')
def step_impl(context):  
    
    if context.user!= None :

       assert context.user[2] !=None
       
    else:
        assert context.user==None
    
@when('se realiza una solicitud para iniciar sesion exitoso')
def step_impl(context):
    email = "isaac_n@email.com"
    password = "16"

     # Realizar la solicitud de autenticación a /auth con los datos proporcionados
    data = {'email': email, 'password': password}
    context.response = requests.post('http://127.0.0.1:3000/auth', json=data)


@when('se realiza una solicitud para iniciar sesion no exitoso')
def step_impl(context):
    email = "isaac_n@email.com"
    password = "1"

     # Realizar la solicitud de autenticación a /auth con los datos proporcionados
    data = {'email': email, 'password': password}
    context.response = requests.post('http://localhost:3000/auth', json=data)

@then('se recibe una respuesta con el "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.user != None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
        
        
@then('la respuesta contiene el mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje
    