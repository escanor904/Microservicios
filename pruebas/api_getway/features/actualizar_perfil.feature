Feature: Actualización de perfil

  Scenario: Actualización exitosa de perfil
    # Requerimiento:
    Given tener un token válido
    # Acción
    When se realiza una solicitud para actualizar el perfil con datos válidos
    # Resultado esperado
    Then se recibe una respuesta exitosa con el "código de estado 200"
    And la respuesta contiene el mensaje "Perfil actualizado exitosamente"

  Scenario: Error al actualizar perfil debido a falta de token
    # Requerimiento:
    Given no se tiene un token válido
    # Acción
    When se realiza una solicitud para actualizar el perfil sin proporcionar un token
    # Resultado esperado
    Then se recibe una respuesta con el "Perfil no actualizado, intente denuevo"
