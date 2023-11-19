Feature: Inicio de sesion


  Scenario: Se valida el usuario 

    #Requerimiento: 
    #tener un usuario previamente registrado

     Given tener un usuario previamente registrado en el sistema
     And tener la contraseña para el usuario
     #Acción
     When se realiza la solicitud al servidor 
     #Condicion extra
     #lo que se espera
     Then se libera el mensaje de respuesta "status code:200"

  Scenario: No sea valido el usuario 
    
    Given no tener un usuario que no este registrado en el sistema
    And tener la contraseña para el usuario
     #Accion
     When se realiza la solicitud al servidor
     #lo que se espera
     Then se libera el mensaje de respuesta "status code:400"

