from behave import given, when, then
import requests

db_config = {
    # Configuración de la base de datos
    'dbname': 'profile_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5433'
}

@given('ingresar a la ruta que se desea consultar')
def api_en_ejecucion(context):
    pass
    

@when('se hace una solicitud a la ruta')
def solicitud_a_ruta(context):
    context.response = requests.get('http://localhost:8080/')  

@then('se recibe una respuesta con el mensaje "{mensaje}"')
def verificar_respuesta_mensaje(context, mensaje):
    assert mensaje in context.response.text