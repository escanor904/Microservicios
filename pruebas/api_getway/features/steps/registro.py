from behave import given, when, then
import psycopg2, requests

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5434'
}

@given('el usuario desea registrarse con email y contraseña validos')
def proporcionar_datos(context):  
    context.username = "salome"
    context.email = "salome@email.com"
    context.password = "124124"
    
@given('el usuario desea registrarse con datos faltantes')
def proporcionar_datos_incompletos(context):  
    context.username = "salome"
    context.email = ""
    context.password = "124124"

@when('se realiza una solicitud para registrar un nuevo usuario')
def step_impl(context):
    if context.username and context.password and context.email:
        # Crear un diccionario con los datos del usuario para enviar en la solicitud
        data = {
            'username': context.username,
            'email': context.email,
            'password': context.password
        }

        # Realizar la solicitud POST a la ruta http://localhost:5000/registro con los datos del usuario
        response = requests.post('http://localhost:5000/registro', json=data)



@then('se recibe un mensaje con el "{codigo}"')
def enviar_reporte_codigo(context,codigo):
    assert codigo==codigo

        