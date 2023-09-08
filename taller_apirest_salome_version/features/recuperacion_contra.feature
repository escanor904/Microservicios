Feature: recuperación de contraseña

  
  Scenario: Se valida el usuario 
          
    #Requerimiento: 
    #tener un usuario previamente registrado
    Given ser un usuario previamente registrado
     #Acción
     When se realiza la solicitud al servidor 
     #Condicion extra
     Then se obtiene el mensaje de respuesta "status code:200"

     
      

  Scenario: No se valida el usuario 
     Given tener un usuario que no este registrado 
     When se realiza la solicitud al servidor
     Then se obtiene el mensaje de respuesta "status code:400"

    #Given establecer la conexion con la base de datos
     #Acción
     #When Obtener el correo electrónico proporcionado por el usuario
     #Condicion extra
     #And Buscar al usuario en la base de datos por su email
     #And Generar un token de recuperación de contraseña
     #Resultado esperado
     #Then se muestra el mensaje No existe ningún registro correspondiente a este usuario en la base de datos


