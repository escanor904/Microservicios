Feature: Mostrar perfil

  Scenario: Mostrar perfil con token valido
    # Requerimiento:
    Given se tiene un token valido
    # Acción
    When realizo una solicitud para mostrar el perfil con el token
    # Resultado esperado
    Then recibo un mensaje con el "codigo de estado 200" 
    And la respuesta contiene el mensaje "Visulizacion de perfil exitosa"

  Scenario: Mostrar perfil con token invalido
    # Requerimiento:
    Given no se tiene un token válido
    # Acción
    When realizo una solicitud para mostrar el perfil con el token
    # Resultado esperado
    Then recibo un mensaje con el "codigo de estado 400" 
    And la respuesta contiene el mensaje "Visulizacion de perfil no exitosa"
