Feature: Cambio de contrasena

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Contraseña actualizada con éxito
          
    #Requerimientos: 
    Given establecer la conexion con la base de datos
    And Obtener la identidad del usuario desde el token JWT
     #Acción
     When Obtener los datos de la nueva contraseña desde la carga JSON de la solicitud
     #Condicion extra
     And Actualizar la contraseña del usuario en la base de datos 
     #Resultado esperado
     Then se muestra el mensaje "Contraseña actualizada exitosamente"

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: La contraseña no pudo ser modificada
    #Requerimientos: 
    Given establecer la conexion con la base de datos
    And Obtener la identidad del usuario desde el token JWT
     #Acción
     When Obtener los datos de la nueva contraseña desde la carga JSON de la solicitud
     #Condicion extra
     And Actualizar la contraseña del usuario en la base de datos       

     Then se muestra el mensaje "Invalid header string: ..." 