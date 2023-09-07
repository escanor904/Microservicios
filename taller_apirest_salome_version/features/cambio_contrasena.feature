Feature: Cambio de contrasena

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Contraseña actualizada con éxito
          
    #Requerimientos: 
    Given establecer la conexion CC
    And Obtener la identidad del usuario desde el token JWT: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNyaXN0aWFub19yQGVtYWlsLmNvbSJ9.X4R3IAM-SMtaIHnT6G_xzgfZx5H2X0jh9Ju4uRWyIco"
     #Acción
     When La contrasena para la actualizacion es "16"
     #Condicion extra
     And Actualizar la contraseña del usuario en la base de datos 
     #Resultado esperado
     Then se muestra el mensaje de exito "Contraseña actualizada exitosamente"

  #Este caso de prueba se enfocará en que las credenciales son validas
  #Scenario: La contraseña no pudo ser modificada
    #Requerimientos: 
    #Given establecer la conexion 
    #And Obtener la identidad del usuario con un token invalido: "fyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNyaXN0aWFub19yQGVtYWlsLmNvbSJ9.X4R3IAM-SMtaIHnT6G_xzgfZx5H2X0jh9Ju4uRWyIco"
     #Acción
     #When La contrasena para la actualizacion es "16"
     #Condicion extra
     #And Actualizar la contraseña del usuario en la base de datos       

     #Then se muestra el mensaje de fallo "Invalid header string: ..." 