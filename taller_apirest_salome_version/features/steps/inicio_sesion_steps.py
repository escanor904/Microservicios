from behave import given, when, then, step
import psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}




@given('establecer la conexion CC')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    # Aseguro que la coneccion es diferente de null
    assert conn != None



@when('iniciar sesion con el correo "{email}" y clave "{clave}"')
def obtener_datos_de_inicio(context,email,clave):
    # Guardar el email en el contexto para su uso posterior
    context.email=email
    # Guardar la clave en el contexto para su uso posterior
    context.clave=clave
    #Aseguro que el email no venga vacio
    assert email != None, "El correo electrónico no puede ser nulo"
    #Aseguro que el email no venga vacio
    assert clave != None, "La clave no puede ser nula"


@when('Buscar al usuario en la base de datos por su email')
def buscar_usuario_por_email(context):
     
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (context.email,))
    user = cursor.fetchone()
    context.user = user
    assert user != None
        
@when('Validar la contraseña')
def validar_contrasena(context):
    assert context.user and context.user[2] == context.clave
    
    
@then('recibo la respuesta CC')
def enviar_reporte(context):
    if context.failed:
        print("Credenciales inválidas")
    assert context.failed is False
     
            
        
        

    

    

    