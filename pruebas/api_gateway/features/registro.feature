Feature: Registro de un usuario

  Scenario: Registro de un usuario exitoso
    # Requerimiento:
    Given el usuario desea registrarse con email y contraseña validos
    # Acción
    When se realiza una solicitud para registrar un nuevo usuario
    # Resultado esperado
    Then se recibe un mensaje con el "código de estado 200" 
    And la respuesta contiene el mensaje "Usuario registrado exitosamente"
  
  Scenario: Registro de un usuario no exitoso
    # Requerimiento:
    Given el usuario desea registrarse con datos faltantes
    # Acción
    When se realiza una solicitud para registrar un nuevo usuario
    # Resultado esperado
    Then se recibe un mensaje con el "código de estado 400" 
    And la respuesta contiene el mensaje "El usuario no se pudo registrar"