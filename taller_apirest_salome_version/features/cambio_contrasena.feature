Feature: Cambio de contrasena

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Contraseña actualizada con éxito
          
    #Requerimientos: 
    Given tener un usuario en sesion
    And tener una contrasena valida
     #Acción
     When hacer la solicitud a el servidor que actualice la contrasena en la base de datos
     #Resultado esperado
     Then se muestra el mensaje que retorna el server "Contraseña actualizada exitosamente    status code:200"

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Contraseña actualizada con éxito
          
    #Requerimientos: 
    Given no tener un un usuario en sesion
    And tener una contrasena no valida
     #Acción
     When hacer la solicitud a el servidor que actualice la contrasena en la base de datos
     #Resultado esperado
     Then se muestra el mensaje que retorna el server "error     status code:400"   

