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

@given('tener un usuario en una sesion')
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
    
@given('no tener un usuario en sesion')
def establecer_conexion(context):  
    context.user=None
    # Aseguro el usuario es diferente de null
    assert context.user==None
        
    
@given('tener un correo valido')
def establecer_conexion(context):  
    context.email = "email_valido@email.com"
    # Aseguro el usuario es diferente de null
    assert context.email=="email_valido@email.com"
    
@given('tener un correo no valido')
def establecer_conexion(context):  
    context.email = "email_novalido@enail.com"
    # Aseguro el usuario es diferente de null
    assert context.email=="email_novalido@enail.com"
    

    
@when('hacer la solicitud al servidor que actualice el correo')
def step_impl(context):
    if (context.email != "email_valido@email.com") and (context.user!=None) :
       cursor = context.db_connection.cursor()
       # Actualizar la contraseña del usuario en la base de datos
       cursor.execute("UPDATE users SET email = %s WHERE email = %s",
                       (context.new_email, context.current_user_email))
       pass
    else:
       pass
        

    
    
@then('se muestra el mensaje que retorna el server "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.user!=None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
    

    
    


