from behave import given, when, then, step
from behave import *
import psycopg2
db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5434'
}

@given('el usuario proporciona los datos validos')
def proporcionar_datos(context):  
    context.username = "salome"
    context.email = "salome@email.com"
    context.password = "124124"
    
@given('el usuario proporciona los datos incompletos')
def proporcionar_datos_incompletos(context):  
    context.username = "salome"
    context.email = ""
    context.password = "124124"

@given('el usuario proporciona los datos de un usuario existente')
def proporcionar_datos_existentes(context):  
    context.username = "salome"
    context.email = "salome@email.com"
    context.password = "124124"
    
@when('se registra en la aplicacion')
def step_impl(context):
    if context.username and context.password and context.email:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (context.username,))
        existe_usuario = cursor.fetchone()[0]

        if existe_usuario == 0:
            cursor.execute("INSERT INTO users (username, hashed_password, email) VALUES (%s, %s, %s)",
                    (context.username, context.password, context.email)
                )
        conn.commit()


@then('se recibe una respuesta con el "{codigo}"')
def enviar_reporte_codigo(context,codigo):
    assert codigo==codigo

        
@then('la respuesta contiene el mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje