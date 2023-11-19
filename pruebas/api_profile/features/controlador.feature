Feature: Obtencion de logs por aplicación

  Scenario: Obtener logs por aplicación con datos válidos
    # Requerimiento:
    Given tener logs previamente registrados en el sistema
    # Acción
    When se realiza una solicitud con una aplicacion que existe en la base de datos
    # Resultado esperado
    Then retorna una lista paginada de logs para la aplicación especificada con el "código de estado 200"

  Feature: Verificar el controlador de índice

  Scenario: Verificar la solicitud GET en /index
    # Requerimiento:
    Given que la API está en ejecución
    # Acción
    When se hace una solicitud a la ruta
    # Resultado esperado
    Then se recibe una respuesta con el mensaje "Hello there visitor"
