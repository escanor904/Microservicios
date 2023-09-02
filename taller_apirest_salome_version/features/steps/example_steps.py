# -- FILE: features/steps/example_steps.py
# behave nos permite la automatización de escenarios que estab hechos con BDD
# BDD: 
#Gherkin: lenguaje que comprenden todos los miembros de la organización
from behave import given, when, then, step

# given son los prerrequisitos
@given('tenemos behave instalado')
def step_impl(context):
    pass

# when es una acción
@when('implementamos {number:d} pruebas')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

# este es el resultado esperado
@then('behave prueba todo por nosotros!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0