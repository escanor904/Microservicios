from behave import given, when, then, step
import psycopg2, requests

db_config = {
    # Configuración de la base de datos
    'dbname': 'logs_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': '127.0.0.1',
    'port': '5435'
}

@given('tener logs registrados en el sistema')
def tener_logs_registrados(context):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Realizar una consulta para verificar si existen registros de logs en la base de datos
    cursor.execute("SELECT COUNT(*) FROM logs")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert count > 0, "No hay registros de logs en la base de datos"

@when('se realiza una solicitud para obtener todos logs')
def realizar_solicitud_obtener_logs(context):
    url = 'http://localhost:8081/logs'  # URL de tu API para obtener logs
    response = requests.get(url)
    context.response = response

@then('se retorna una lista paginada de todos los logs existentes con el "código de estado 200"')
def verificar_respuesta_exitosa_obtener_logs(context):
    assert context.response.status_code == 200

    response_data = context.response.json()

    # Verificar si la clave 'logs' está presente en la respuesta
    if 'logs' in response_data:
        logs_list = response_data['logs']

        # Verificar si la lista de logs no está vacía
        assert len(logs_list) > 0, "La lista de logs está vacía o no contiene registros"
    else:
        # Si no hay clave 'logs', la lista se considera vacía
        print("La respuesta no contiene la lista de logs o está vacía")
