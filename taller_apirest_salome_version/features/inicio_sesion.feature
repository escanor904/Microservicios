Feature: Inicio de sesion

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Iniciar sesion con las credenciales validas 
          
    #Requerimiento: 
    Given tener un usuario ya registrado en el sistema
    And tener la contraseña para el usuario
     #Acción
     When realizar la solicitud a la base de datos
     #Resultado esperado
     Then se captura el mensaje de respuesta "token:deujde7d6ed7ed57de......  status code:200"


  Scenario: Iniciar sesion con credenciales invalidas
    #Requerimiento: 
    Given tener un usuario ya registrado en el sistema
    And tener la contraseña para el usuario
     #Acción
     When realizar la solicitud a la base de datos
     #Resultado esperado
     Then se captura el mensaje de respuesta ""mensaje": "Credenciales invalidas  status code:400"
          

