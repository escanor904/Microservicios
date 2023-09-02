Feature: Inicio de sesion

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Iniciar sesion con las credenciales validas 
          
    #Requerimiento: 
    Given estar en la dirección asignada a el inicio de sesión
     #Acción
     When Ingreso mi email y mi password
     #Condicion extra
     And envio el formulario 
     #Resultado esperado
     Then recibo el codigo jwt

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Iniciar sesion con las credenciales invalidas
          
    #Requerimiento: 
    Given estar en la dirección asignada a el inicio de sesión
     #Acción
     When Ingreso mi email y mi password
     #Condicion extra
     And envio el formulario 
     #Resultado esperado
     Then se muestra el mensaje de "Credenciales invalidas"   

