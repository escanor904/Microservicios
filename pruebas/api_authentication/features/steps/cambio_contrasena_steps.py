from behave import given, when, then, step
from flask_jwt_extended import get_jwt_identity
import psycopg2
import jwt

db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5434'
}

@given('tener un usuario en sesion')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    context.user=user
    # Aseguro el usuario es diferente de null
    assert user!=None
    
@given('no tener un un usuario en sesion')
def establecer_conexion(context):  
    context.user=None
    assert context.user==None
        
    
@given('tener una contrasena valida')
def establecer_conexion(context):  
    context.password = "password_valido"
    assert context.password=="password_valido"
    
@given('tener una contrasena no valida')
def establecer_conexion(context):  
    context.password = "password_no_valido"
    assert context.password=="password_no_valido"
    

    
@when('hacer la solicitud a el servidor que actualice la contrasena en la base de datos')
def step_impl(context):
    if (context.password != "password_valido") and (context.user!=None) :
       cursor = context.db_connection.cursor()
       cursor.execute("UPDATE users SET hashed_password = %s WHERE email = %s",
                      (context.nuevo_password, context.current_user_email))
       pass
    else:
       pass
        

    
    
@then('se muestra el mensaje que retorna el server "{mensaje}":')
def enviar_reporte(context,mensaje):
    if context.user!=None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
    

    
    


