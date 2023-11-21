import requests, secrets 
from behave import given, when, then

@given('se tiene un usuario está autenticado con un token valido')
def step_impl(context):
    context.token = "sfasgyhtuiyutrewqertghfds"
    
@given('se tiene un usuario está autenticado con un token invalido')
def step_impl(context):
    context.token = "sfasgyhtuiyutrewdddddddddddqertghfds"
    
@when('se realiza una solicitud para mostrar el perfil con el token')
def step_impl(context):
    email = "isaac_n@email.com"
    headers = {'Authorization': f'Bearer {context.token}'}
    url = f'http://127.0.0.1:3000/mostrarPerfil/{email}'  
    context.response = requests.get(url, headers=headers)


@then('se recibe un mensaje con el "{codigo}"')
def enviar_reporte_codigo(context,codigo):
    assert codigo==codigo

        
@then('la respuesta contiene un mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje
