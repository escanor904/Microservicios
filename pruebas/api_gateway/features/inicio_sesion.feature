Feature: Autenticaion de usuarios

  Scenario: Autenticación exitosa
    # Requerimiento:
    Given tener un usuario registrado en el sistema
    And tener la contraseña para el usuario registrado 
    # Acción
    When se realiza una solicitud para iniciar sesion exitoso
    # Resultado esperado
    Then se recibe una respuesta con el "código de estado 200"
    And la respuesta contiene el mensaje "Inicio de sesion exitoso"

  Scenario: Autenticación no exitosa
    # Requerimiento:
    Given no tener un usuario registrado en el sistema
    And tener la contraseña para el usuario registrado
    # Acción
    When se realiza una solicitud para iniciar sesion no exitoso
    # Resultado esperado
    Then se recibe una respuesta con el "código de estado 400"
    And la respuesta contiene el mensaje "Usuario y/o contraseña incorrectas"