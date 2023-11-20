Feature: Verificar el controlador de índice

  Scenario: Verificar la solicitud a /
    # Requerimiento:
    Given ingresar a la ruta que se desea consultar
    # Acción
    When se hace una solicitud a la ruta
    # Resultado esperado
    Then se recibe una respuesta con el mensaje "Hello there visitor"
