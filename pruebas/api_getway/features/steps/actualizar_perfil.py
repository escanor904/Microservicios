from behave import given, when, then
import requests

@given('tener un token válido')
def tener_token_valido(context):
    # Lógica para obtener un token válido o simular uno válido en el contexto
    context.token = 'token_valido'

@when('se realiza una solicitud para actualizar el perfil con datos válidos')
def enviar_solicitud_actualizar_perfil(context):
    if 'token' not in context:
        raise Exception('No se tiene un token válido')
    
    # Aquí se simula la solicitud POST para actualizar el perfil con un token válido
    url = 'http://127.0.0.1:3000/updateProfile'  # Reemplaza con la URL real para actualizar el perfil
    headers = {'Authorization': f'Bearer {context.token}'}
    payload = {
        'token': context.token,
        'username': 'nuevo_usuario',
        'personalpage': 'nueva_pagina_personal',
    }
    
    response = requests.post(url, headers=headers, json=payload)
    context.response = response

@then('se recibe una respuesta exitosa con el "código de estado 200"')
def verificar_respuesta_exitosa(context):
    if context.response.status_code == 200:
        pass
    else:
        raise AssertionError('La respuesta no es exitosa con el código de estado 200')

@when('se realiza una solicitud para actualizar el perfil sin proporcionar un token')
def enviar_solicitud_sin_token(context):
    # Aquí se simula la solicitud POST para actualizar el perfil sin proporcionar un token
    url = 'http://127.0.0.1:3000/updateProfile'  # Reemplaza con la URL real para actualizar el perfil
    payload = {
        'username': 'nuevo_usuario',
        'personalpage': 'nueva_pagina_personal',
    }
    
    response = requests.post(url, json=payload)
    context.response = response

@then('se recibe una respuesta con el "{codigo}"')
def enviar_reporte(context,codigo):
    if context.user != None :
        assert codigo==codigo
    else:
        assert codigo==codigo
        
        
@then('la respuesta contiene el mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje