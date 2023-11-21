Feature: Actualizar perfil de usuario

  Scenario: Actualizar el perfil de un usuario autenticado con datos válidos
    # Requerimiento:
    Given iniciar sesion en el perfil que se quiere actualizar
    #Acción
    When se actualiza el perfil del usuario con datos válidos
    # Resultado esperado
    Then se recibe una respuesta con el "codigo 200"
    And la respuesta contiene el mensaje "Perfil actualizado exitosamente"

  Scenario: Actualizar el perfil de un usuario autenticado con datos inválidos
    # Requerimiento:
    Given iniciar sesion en el perfil que se quiere actualizar
    #Acción
    When se intenta actualizar el perfil del usuario con datos incorrectos
    # Resultado esperado
    Then se recibe una respuesta con el "codigo 400"
    And la respuesta contiene el mensaje "El perfil no se actualizo con exito, datos invalidos"

