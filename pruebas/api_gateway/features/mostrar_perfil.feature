Feature: Mostrar perfil

  Scenario: Mostrar el perfil exitoso
    # Requerimiento:
    Given se tiene un usuario está autenticado con un token valido
    # Acción
    When se realiza una solicitud para mostrar el perfil con el token
    # Resultado esperado
    Then se recibe un mensaje con el "codigo de estado 200" 
    And la respuesta contiene un mensaje "Visulizacion de perfil exitosa"
  
  Scenario: Mostrar perfil no exitoso
    # Requerimiento:
    Given se tiene un usuario está autenticado con un token invalido
    # Acción
    When se realiza una solicitud para mostrar el perfil con el token
    # Resultado esperado
    Then se recibe un mensaje con el "codigo de estado 400" 
    And la respuesta contiene un mensaje "Visulizacion de perfil no exitosa"
    