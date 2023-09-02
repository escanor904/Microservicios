Feature: Cambio de contrasena

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: Contraseña actualizada con éxito
          
    #Requerimiento: 
    Given estar en la dirección asignada a el cambio de contrasena
     #Acción
     When se introduce la nueva contrasena
     #Condicion extra
     And envio el formulario 
     #Resultado esperado
     Then se muestra el mensaje "Contrasena actualizada exitosamente"

  #Este caso de prueba se enfocará en que las credenciales son validas
  Scenario: La contraseña no pudo ser modificada
          
    #Requerimiento: 
    Given estar en la dirección asignada a el cambio de contrasena
     #Acción
     When se introduce la nueva contrasena
     #Condicion extra
     And envio el formulario 
     #Resultado esperado
     Then se muestra el mensaje "Invalid header string: ..." 