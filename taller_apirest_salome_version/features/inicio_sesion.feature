Feature: Inicio de sesion

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Iniciar sesion con las credenciales validas 
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When iniciar sesion con el correo "cristiano_r@email.com" y clave "15"
     #Condicion extra
     And Buscar al usuario en la base de datos por su email
     And Validar la contraseña
     #Resultado esperado
     Then recibo la respuesta



  #Este caso de prueba se enfocará en que las credenciales son validas
  #Scenario: Iniciar sesion con las credenciales invalidas
          
    #Requerimiento: 
   # Given establecer la conexion con la base de datos
     #Acción
    # When iniciar sesion con el correo "el_bicho@email.com" y clave "15"
     #Condicion extra
     #And Buscar al usuario en la base de datos por su email
     #And Validar la contraseña
     #Resultado esperado
     #Then recibo la respuesta  

