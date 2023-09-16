import json
import jsonschema
from jsonschema import validate
from faker import Faker

# Cargar el esquema JSON desde el archivo "registro_schema.json"
with open("listado_paginado_schema.json", "r") as schema_file:
    schema = json.load(schema_file)

# Crea una instancia de Faker
fake = Faker()

# Genera datos aleatorios que cumplan con el esquema
data = {
    # Genera un número aleatorio entre 1 y 100 (puedes ajustar los límites según tus necesidades)
    "tamano": fake.random_number(digits=2, fix_len=True),
    "pagina": fake.random_number(digits=2, fix_len=True)
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