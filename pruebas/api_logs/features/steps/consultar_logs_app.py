from behave import given, when, then
import requests
import psycopg2

db_config = {
    # Configuración de la base de datos
    'dbname': 'logs_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost',
    'port': '5435'
}

@given('tener logs previamente registrados en el sistema')
def tener_logs_previamente_registrados(context):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    count = cursor.fetchone()[0]

    context.existen_logs = count > 0

    cursor.close()
    conn.close()


@when('se realiza una solicitud con una aplicacion que existe en la base de datos')
def realizar_solicitud_obtener_logs_aplicacion(context):
    application = "api_users"  # Reemplaza esto con el nombre de la aplicación válido
    context.response = requests.get(f"http://localhost:8081/logs/{application}")

    # Verificar si la solicitud devuelve un código 200 (éxito)
    if context.response.status_code == 200:
        logs = context.response.json()
        if len(logs) == 0:
            print(f"No existen logs para la aplicación '{application}'")
        else:
            # Realizar acciones adicionales si hay logs disponibles
            print("Lista de logs para la aplicación:")
            for log in logs:
                print(log)
    else:
        print(f"La solicitud no se completó con éxito. Código de estado: {context.response.status_code}")


@then('retorna una lista paginada de logs para la aplicación especificada con el "código de estado 200"')
def verificar_respuesta_exitosa(context):
    assert context.response.status_code == 200

    logs = context.response.json()
    assert isinstance(logs, list)

    if len(logs) == 0:
        print("La respuesta no contiene ningún log.")
    else:
        print("Lista de logs:")
        for log in logs:
            assert isinstance(log, list)  # Verificar si cada log es una lista
            # Verificar la estructura interna de cada log en la lista
            for item in log:
                assert isinstance(item, (int, str))  # Verificar tipos de datos esperados
                # Puedes agregar más aserciones según la estructura real de tus logs
                print(item)

        
@then('la lista de logs contiene registros únicamente para la aplicación especificada y que cumplen con los criterios de filtro')
def verificar_logs_aplicacion_especificada(context):
    logs = context.response.json()
  
@when('se realiza una solicitud con una aplicacion que no existe en la base de datos')
def realizar_solicitud_aplicacion_no_existente(context):
    application_no_existente = "aplicacion_inexistente"  # Nombre de una aplicación que no existe en la base de datos
    context.response = requests.get(f"http://localhost:8081/logs/{application_no_existente}")

@then('se retorna un mensaje indicando que no se encontraron registros para la aplicación con el "código de estado 400"')
def verificar_no_registros_aplicacion(context):
    assert context.response.status_code == 400

    try:
        response_data = context.response.json()
        assert 'message' in response_data
        assert f"No se encontraron registros para la aplicación '{context.application}'" == response_data['message']
    except ValueError:
        print("La respuesta no es un JSON válido:")
        print(context.response.text)  # Imprime el texto de la respuesta para debug
