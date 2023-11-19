from behave import given, when, then, step
from flask_jwt_extended import get_jwt_identity
import requests, psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'logs_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5435'
}

@given('un usuario realice alguna accion en el sistema')
def realizar_accion(context):
    url = 'http://127.0.0.1:5000/inicio_sesion'  # URL de la API de inicio de sesión
    headers = {'Content-Type': 'application/json'}
    data = {
        "email" : "isaac_n@email.com",
        "password" : "16"
    }

    response = requests.post(url, json=data, headers=headers)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Guardar el token en el contexto para su uso posterior
        context.token = response.json().get('token')
    else:
        # Si la solicitud no fue exitosa, puedes manejar el error según sea necesario
        print('No se pudo iniciar sesión')

@when('se realiza una solicitud con los datos del nuevo log')
def enviar_solicitud_post(context):
    datos_nuevo_log = {
        'application': 'nombre_aplicacion',
        'log_type': 'tipo_log',
        'description': 'descripcion_del_log'
    }

    url = 'http://127.0.0.1:8081/logs' 
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=datos_nuevo_log, headers=headers)
    context.response = response

@then('se crea el log exitosamente y retorna un mensaje de éxito con el "código de estado 201"')
def verificar_creacion_exitosa(context):
    assert context.response.status_code == 201
    assert 'Log creado exitosamente' in context.response.json()['message']

@when('se realiza una solicitud sin proporcionar ciertos datos obligatorios del nuevo log')
def enviar_solicitud_post_sin_datos_obligatorios(context):
    # Crear datos incompletos del nuevo log sin algunos campos requeridos
    datos_incompletos = {
        'log_type': 'tipo_log',
        # Faltan otros campos obligatorios
    }

    url = 'http://localhost:8081/logs'  # URL de tu API
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=datos_incompletos, headers=headers)
    context.response = response

@then('se retorna un mensaje de error indicando datos faltantes con el "código de estado 400"')
def verificar_respuesta_error(context):
    # Verifica si el código de estado devuelto por la API es 400
    assert context.response.status_code == 400

    # Parsea la respuesta para obtener el mensaje de error
    response_data = context.response.json()
    
    # Verifica si el mensaje de error esperado está presente en la respuesta
    expected_error_message = 'Datos faltantes'
    assert 'message' in response_data
    assert expected_error_message in response_data['message'], f"El mensaje de error esperado '{expected_error_message}' no está presente en la respuesta"
