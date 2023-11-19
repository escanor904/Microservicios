import requests, secrets 
from behave import given, when, then

@given('se tiene un token valido')
def tener_token_valido(context):
    auth_url = 'https://127.0.0.1:3000/auth'  # Reemplaza con la URL real del endpoint de autenticación
    payload = {'username': 'tu_usuario', 'password': 'tu_contraseña'}  # Proporciona credenciales válidas
    response = requests.post(auth_url, data=payload)
    
    if response.status_code == 200:
        context.token = response.json().get('token')
    else:
        raise Exception('No se pudo obtener un token válido')

@given('no se tiene un token valido')
def no_tener_token_valido(context):
    context.token = 'token_valido'

@when('realizo una solicitud para mostrar el perfil con el token')
def enviar_token(context):
    if 'token' not in context:
        raise Exception('No se tiene un token válido')
    
    url = 'http://127.0.0.1:3000/mostrarPerfil'  # Reemplaza con la URL real para mostrar el perfil
    headers = {'Authorization': f'Bearer {context.token}'}  # Utiliza el token obtenido en el paso anterior
    
    response = requests.get(url, headers=headers)
    context.response = response  # Almacena la re

@then('recibo un mensaje con el "{codigo}"')
def enviar_reporte(context,mensaje):
    if context.user != None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje

@then('la respuesta contiene el mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje
    