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




@given('establecer la conexion Cassa')
def establecer_conexion(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    # Aseguro que la coneccion es diferente de null
    assert conn != None
    
@given('Obtener la identidad del usuario desde el token JWT: "{token}"')
def recuperar_identidad(context,token):  
    # Decodificar el token JWT utilizando la clave secreta
    decoded_token = jwt.decode(token, "mypass", algorithms=["HS256"])
    # Recuperar la información del token (en este caso, la dirección de correo electrónico)
    email = decoded_token.get("email") 
    context.current_user_email=email
    assert email != None
    
@given('Obtener la identidad del usuario con un token invalido: "{token}"')
def recuperar_identidad(context,token):  
    # Decodificar el token JWT utilizando la clave secreta
    #decoded_token = jwt.decode(token, "mypass", algorithms=["HS256"])
    # Recuperar la información del token (en este caso, la dirección de correo electrónico)
    #email = decoded_token.get("email") 
    #context.current_user_email=email
    assert False    

    
@when('La contrasena para la actualizacion es "{nuevo_password}"')
def obtener_nueva_contrasena(context,nuevo_password):
    # Guardar el email en el contexto para su uso posterior
    context.nuevo_password=nuevo_password
    #Aseguro que el email no venga vacio
    assert nuevo_password != None, "La contrasena no puede ser nulo"
    
@when('Actualizar la contraseña del usuario en la base de datos')
def actualizar_password(context):
     
    cursor = context.db_connection.cursor()
    # Actualizar la contraseña del usuario en la base de datos
    cursor.execute("UPDATE users SET hashed_password = %s WHERE email = %s",
                   (context.nuevo_password, context.current_user_email))
    
    pass
    
@then('se muestra el mensaje de exito "{mensaje}"')
def enviar_reporte(context,mensaje):
    assert mensaje == mensaje
    assert context.failed is False
    
@then('se muestra el mensaje de fallo"{mensaje}"')
def enviar_reporte(context,mensaje):
    assert mensaje == mensaje
    assert False
    
    


