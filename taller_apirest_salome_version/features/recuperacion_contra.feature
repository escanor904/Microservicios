Feature: recuperación de contraseña

  
  Scenario: Se valida el usuario 
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When Obtener el correo electrónico proporcionado por el usuario
     #Condicion extra
     And Buscar al usuario en la base de datos por su email
     And Generar un token de recuperación de contraseña
     #Resultado esperado
     Then se muestra el token 

    Scenario: No se valida el usuario 
          
    Given establecer la conexion con la base de datos
     #Acción
     When Obtener el correo electrónico proporcionado por el usuario
     #Condicion extra
     And Buscar al usuario en la base de datos por su email
     And Generar un token de recuperación de contraseña
     #Resultado esperado
     Then se muestra el mensaje No existe ningún registro correspondiente a este usuario en la base de datos


