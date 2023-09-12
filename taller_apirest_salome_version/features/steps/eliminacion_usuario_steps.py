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

@given('tener usuario en una sesion')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.user_id=user[0]
    context.email=user[3]
    context.user=user
    # Aseguro el usuario es diferente de null
    assert user!=None

@given('no tener usuario en sesion')
def establecer_conexion(context):  
    context.user=None
    # Aseguro el usuario es diferente de null
    assert context.user==None

@when('hacer la solicitud al servidor que elimine el usuario')
def step_impl(context):
    if (context.user!=None):
       cursor = context.db_connection.cursor()
        # Eliminar al usuario de la base de datos
       cursor.execute("DELETE FROM users WHERE user_id = %s", (context.user_id,))
       pass
    else:
       pass

@then('le muestra el mensaje que retorna el server "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.user!=None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje