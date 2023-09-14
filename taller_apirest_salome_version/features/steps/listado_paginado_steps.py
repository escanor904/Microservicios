from behave import given, when, then, step
import psycopg2


db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}

@given('tener al menos registrado los usuarios que va a consultar')
def registros_bd(context):  
    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(**db_config)
    # Guardar la conexión en el contexto para su uso posterior
    context.db_connection = conn
    cursor = context.db_connection.cursor()

    # Ejecutar una consulta para seleccionar al menos un usuario
    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()
    if user:
        context.email = user[3]
        context.user = user
    cursor.close()


@when('proporcionar los parametros de paginacion {pagina} con un tamaño de página de {tamano_pagina}')
def solicitar_lista_de_usuarios(context, pagina, tamano_pagina):
    # Convierte los valores de página y tamaño de página en enteros
    pagina = int(pagina)
    tamano_pagina = int(tamano_pagina)

    # Verifica si los valores son válidos (mayores o iguales a 1)
    if pagina < 1 or tamano_pagina < 1:
        context.error_message = "Los parámetros de paginación deben ser mayores o iguales a 1"
    else:
        # Recuperar la conexión a la base de datos del contexto
        conn = context.db_connection

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Calcular el desplazamiento basado en la página y el tamaño de la página
        offset = (pagina - 1) * tamano_pagina

        # Consulta SQL para obtener la lista de usuarios con paginación
        query = f"SELECT * FROM users LIMIT {tamano_pagina} OFFSET {offset}"

        # Ejecutar la consulta
        cursor.execute(query)

        # Obtener la lista de usuarios en la página actual
        users = cursor.fetchall()

        # Guardar la lista de usuarios en el contexto para su uso posterior
        context.paginated_users = users

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
    # # Convierte los valores de página y tamaño de página en enteros
    # pagina = int(pagina)
    # tamano_pagina = int(tamano_pagina)

    # if pagina < 1 or tamano_pagina < 1:
    #     pass

    # # Recuperar la conexión a la base de datos del contexto
    # conn = context.db_connection

    # # Crear un cursor para ejecutar consultas
    # cursor = conn.cursor()

    # # Calcular el desplazamiento basado en la página y el tamaño de la página
    # offset = (pagina - 1) * tamano_pagina

    # # Consulta SQL para obtener la lista de usuarios con paginación
    # query = f"SELECT * FROM users LIMIT {tamano_pagina} OFFSET {offset}"

    # # Ejecutar la consulta
    # cursor.execute(query)

    # # Obtener la lista de usuarios en la página actual
    # users = cursor.fetchall()

    # # Guardar la lista de usuarios en el contexto para su uso posterior
    # context.paginated_users = users

    # # Cerrar el cursor y la conexión
    # cursor.close()
    # conn.close()

@then('se recibe una respuesta con "{codigo}"')
def enviar_reporte_codigo_p(context,codigo):
    assert codigo==codigo

        
@then('la respuesta contiene una lista de {cantidad} usuarios')
def verificar_lista_de_usuarios(context, cantidad):
    # Convierte la cantidad deseada en un entero
    cantidad = int(cantidad)

    # Verifica que la respuesta contenga la cantidad correcta de usuarios
    assert len(context.paginated_users) == cantidad



@then('la respuesta contiene un mensaje "{mensaje}"')
def enviar_reporte_mensaje_p(context,mensaje):
    assert mensaje==mensaje