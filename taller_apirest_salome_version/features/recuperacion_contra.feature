Feature: recuperación de contraseña

  
  Scenario: Se valida el usuario 
          
    #Requerimiento: 
    Given estar en la dirección asignada a recuperacion de contrasena
     #Acción
     When se introduce la direccion del usuario
     #Condicion extra
     And se envia el formulario 
     #Resultado esperado
     Then se muestra el token 

    Scenario: No se valida el usuario 
          
    #Requerimiento: 
    Given estar en la dirección asignada a recuperacion de contrasena
     #Acción
     When se introduce la direccion del usuario
     #Condicion extra
     And se envia el formulario 
     #Resultado esperado
     Then se muestra el mensaje No existe ningún registro correspondiente a este usuario en la base de datos


