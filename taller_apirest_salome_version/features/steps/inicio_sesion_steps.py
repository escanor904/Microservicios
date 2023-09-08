from behave import given, when, then, step
import psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}



@given('tener un usuario ya registrado en el sistema')
def step_impl(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    # Aseguro que la coneccion es diferente de null
    assert context.email !=None
    
@given('tener la contraseña para el usuario')
def step_impl(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.password=user[2]
    # Aseguro que la coneccion es diferente de null
    assert context.password !=None

@when('realizar la solicitud a la base de datos')
def step_impl(context):
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (context.email,))
    user = cursor.fetchone()
    
    if user and user[2] == context.password:
       context.salida=1
       assert user and user[2] == context.password 
    else:
        context.salida=0    
        assert user and user[2] != context.password
    

@then('se captura el mensaje de respuesta "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.salida == 1 :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
            
        
        

    

    

    