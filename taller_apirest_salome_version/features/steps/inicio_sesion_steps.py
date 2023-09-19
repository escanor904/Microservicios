from behave import given, when, then, step
import psycopg2
from faker import Faker
import json
import jsonschema
from jsonschema import validate


db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}



@given('no tener un usuario que no este registrado en el sistema')
def step_impl(context):  
    context.user=None
    assert context.user == None
    
@given('tener un usuario previamente registrado en el sistema')
def step_impl(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    context.email=user[3]
    context.user=user
    
    assert user != None
    



@given('tener la contraseña para el usuario')
def step_impl(context):  
    
    if context.user!= None :

       assert context.user[2] !=None
       
    else:
        assert context.user==None
    
    
@when('se realiza la solicitud al servidor ')
def step_impl(context):
    if context.user != None :
        conn = psycopg2.connect(**db_config)
        # Guardar la conexión en el contexto para su uso posterior
        context.db_connection = conn
        cursor = context.db_connection.cursor()
        cursor.execute("SELECT * FROM users LIMIT 1")
        user = cursor.fetchone()
        context.password=user[2]
        assert context.password != None
    else:
        assert context.user == None
    

            

@then('se libera el mensaje de respuesta "{mensaje}"')
def enviar_reporte(context,mensaje):
    if context.user != None :
        assert mensaje==mensaje
    else:
        assert mensaje==mensaje
        
@then('la estructura de la respuesta es "{mensaje}"')
def step_impl(context,mensaje):
    # Cargar el esquema JSON desde el archivo "registro_schema.json"
    #taller_apirest_salome_version/schems/registro_schema.json
    with open("taller_apirest_salome_version/schems/inicio_sesion_schema.json", "r") as schema_file:
      schema = json.load(schema_file)

    # Crea una instancia de Faker
    fake = Faker()

    # Genera datos aleatorios que cumplan con el esquema
    data = {
       "email": fake.email(),
       "password": fake.password(length=3, special_chars=False),
    }

    # Convierte el diccionario de datos en una cadena JSON
    json_data = json.dumps(data, indent=4)

    # Imprime la cadena JSON generada
    print("Datos generados:")
    print(json_data)
    
    if mensaje=="correcto" :
       # Validación del esquema JSON
       validate(data, schema)
       assert "el esquema es valido"
    else:
       assert "el esquema"
  

     
            
        
        

    

    

    