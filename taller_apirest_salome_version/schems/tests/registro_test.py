import json
import jsonschema
from jsonschema import validate
from faker import Faker

# Cargar el esquema JSON desde el archivo "registro_schema.json"
#taller_apirest_salome_version/schems/registro_schema.json
with open("../schems/registro_schema.json", "r") as schema_file:
    schema = json.load(schema_file)

# Crea una instancia de Faker
fake = Faker()

# Genera datos aleatorios que cumplan con el esquema
data = {
    "username": fake.user_name(),
    "password": fake.password(length=3, special_chars=False),
    "email": fake.email()
}

# Convierte el diccionario de datos en una cadena JSON
json_data = json.dumps(data, indent=4)

# Imprime la cadena JSON generada
print("Datos generados:")
print(json_data)

# Validación del esquema JSON
try:
    validate(data, schema)
    print("Los datos generados cumplen con el esquema JSON.")
except jsonschema.exceptions.ValidationError as e:
    print("Error de validación del esquema JSON:")
    print(e)
