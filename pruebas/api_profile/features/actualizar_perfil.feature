Feature: Actualizar perfil de usuario

  Scenario: Actualizar el perfil de un usuario autenticado con datos válidos
    # Requerimiento:
    Given que el usuario está en sesión con un token válido
    #Acción
    When se actualiza el perfil del usuario con datos válidos
    # Resultado esperado
    Then se recibe una respuesta con el "codigo 200"
    And la respuesta contiene el mensaje "Perfil actualizado exitosamente"

  Scenario: Actualizar el perfil de un usuario autenticado con datos inválidos
    # Requerimiento:
    Given que el usuario está en sesión con un token válido
    #Acción
    When se intenta actualizar el perfil del usuario con datos incorrectos
    # Resultado esperado
    Then se recibe una respuesta con el "codigo 400"
    And la respuesta contiene el mensaje "El perfil no se actualizo con exito, datos invalidos"

