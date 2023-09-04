from behave import given, when, then, step
import psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}




@given('establecer la conexion con la base de datos')
def step_impl(context):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    pass


@when('iniciamos sesión con el correo electrónico "{email}" y la clave "{clave}"')
def obtener_datoso_de_inicio(context,email,clave):
    email=email
    assert email != None, "El correo electrónico no puede ser nulo"
    assert clave != None, "La clave no puede ser nula"

@when('Buscar al usuario en la base de datos por su email')
def buscar_usuario_por_email(context):
    context.email

    

    