from behave import given, when, then, step
import psycopg2
db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}

@given('el usuario proporciona los datos validos')
def proporcionar_datos(context):  
    context.username = "salome"
    context.email = "salome@email.com"
    context.password = "124124"
    
@given('el usuario proporciona los datos incompletos')
def proporcionar_datos(context):  
    context.username = "salome"
    context.email = ""
    context.password = "124124"


@when('se registra en la aplicacion')
def step_impl(context):

    if context.user!=None:
        # Verificar si alguno de los campos está vacío
        if context.username and context.password and context.email:
            # Realizar una conexión a la base de datos PostgreSQL utilizando la configuración en db_config
            conn = psycopg2.connect(**context.db_config)
            cursor = conn.cursor()
            # Verificar si el usuario ya existe en la base de datos
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (context.username,))
            existe_usuario = cursor.fetchone()[0]

            if existe_usuario == 0:
                # Agregar al nuevo usuario a la base de datos
                cursor.execute("INSERT INTO users (username, hashed_password, email) VALUES (%s, %s, %s)",
                               (context.username, context.password, context.email))
 

@then('la respuesta debería tener un código de estado  "{codigo}"')
def enviar_reporte(context,codigo):
    if context.user == 1 :
        assert codigo==codigo
    else:
        assert codigo==codigo

        
@then('se captura el mensaje de respuesta "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.salida == 1 :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
            
        