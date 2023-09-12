Feature: Registro del usuario

  #Este caso de prueba se enfocará en que los datos son correctos
  Scenario: Registro exitoso de un nuevo usuario
          
    #Requerimiento: 
    Given el usuario proporciona los datos validos
     #Acción
     When se registra en la aplicacion  
     #Resultado esperado
     Then se recibe una respuesta con el "Codigo estado 201"
     And la respuesta contiene el mensaje "Usuario registrado exitosamente"


  #Este caso de prueba se enfocará el registro del usuario con datos incompletos
  Scenario: Registro del usuario con datos incompletos
    
    #Requerimiento:  
    Given el usuario proporciona los datos incompletos
     #Acción
     When se registra en la aplicacion  
     #Resultado esperado
     Then se recibe una respuesta con el "Codigo de estado 400"
     And la respuesta contiene el mensaje "Diligencie todos los campos"

 #Este caso de prueba se enfocará el registro del usuario que ya existe en la bd
 Scenario: Registro del usuario existente
    
    #Requerimiento: 
    Given el usuario proporciona los datos de un usuario existente
     #Acción
     When se registra en la aplicacion  
     #Resultado esperado
     Then se recibe una respuesta con el "Codigo de estado 409"
     And la respuesta contiene el mensaje "Ese usuario o correo electronico ya esta registrado"
