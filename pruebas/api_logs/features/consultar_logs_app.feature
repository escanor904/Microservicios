Feature: Obtencion de logs por aplicación

  Scenario: Obtener logs por aplicación con datos válidos
    # Requerimiento:
    Given tener logs previamente registrados en el sistema
    # Acción
    When se realiza una solicitud con una aplicacion que existe en la base de datos
    # Resultado esperado
    Then retorna una lista paginada de logs para la aplicación especificada con el "código de estado 200"
    # Condicion extra
    And la lista de logs contiene registros únicamente para la aplicación especificada y que cumplen con los criterios de filtro

  Scenario: Obtener logs por aplicación con aplicación no existente
    # Requerimiento:
    Given tener logs previamente registrados en el sistema
    # Acción
    When se realiza una solicitud con una aplicacion que no existe en la base de datos
    # Resultado esperado
    Then se retorna un mensaje indicando que no se encontraron registros para la aplicación con el "código de estado 400"
