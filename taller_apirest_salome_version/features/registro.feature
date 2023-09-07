Feature: Registro del usuario

  #Este caso de prueba se enfocará en que los datos son correctos
  Scenario: Registro exitoso de un nuevo usuario
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When obtener los datos del usuario con el usuario "caristiano", la contrasena "22" y el correo "cristiano_rr@email.com"
     #Resultado esperado
     Then se recibe una respuesta con codigo estado 201
     And la respuesta contiene el mensaje "Usuario registrado exitosamente"


  #Este caso de prueba se enfocará el registro del usuario con datos incompletos
  Scenario: Registro del usuario con datos incompletos
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When obtener los datos del usuario con el usuario "", la contrasena "22" y el correo "cristiano_rr@email.com"
     #Resultado esperado
     Then se recibe una respuesta con el codigo de estado 400
     And la respuesta contiene el mensaje "Diligencie todos los campos"

 #Este caso de prueba se enfocará el registro del usuario que ya existe en la bd
 Scenario: Registro del usuario existente
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When obtener los datos del usuario con el usuario "Cristiano Ronaldo", la contrasena "15" y el correo "cristiano_r@email.com"
     #Resultado esperado
     Then se recibe una respuesta con el codigo de estado 409
     And la respuesta contiene el mensaje "Ese usuario o corre electronico ya esta registrado"


 #Este caso de prueba se enfocará en el error del servidor
 Scenario: Error en el servidor durante el registro
    #Requerimiento: 
    Given establecer la conexion con la base de datos
    And se simula el error en el servidor
     #Acción
     When obtener los datos del usuario con el usuario "Cristiano Ronaldo", la contrasena "15" y el correo "cristiano_r@email.com"
     #Resultado esperado
     Then se recibe una respuesta con el codigo de estado 500
     And la respuesta contiene el mensaje "Error en el servidor"

