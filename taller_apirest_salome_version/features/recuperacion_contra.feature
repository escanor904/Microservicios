Feature: recuperación de contraseña

  
  Scenario: Se valida el usuario 
          

    Given ser un usuario previamente registrado en el sistema
     #Acción
     When se realiza la solicitud al servidor 
     #lo que se espera
     Then se obtiene el mensaje de respuesta "status code:200"

     
      

  Scenario: No se valida el usuario 
  
    Given tener un usuario que no este registrado en el sistema
     #Accion
     When se realiza la solicitud al servidor
     #lo que se espera
     Then se obtiene el mensaje de respuesta "status code:400"

