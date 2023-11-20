Feature: Obtenecion de los logs

  Scenario: Obtener todos los logs sin filtros
    # Requerimiento:
    Given tener logs registrados en el sistema
    # Acción
    When se realiza una solicitud para obtener todos logs
    # Resultado esperado
    Then se retorna una lista paginada de todos los logs existentes con el "código de estado 200"