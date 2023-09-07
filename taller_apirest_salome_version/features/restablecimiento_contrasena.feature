Feature: Restablecimiento de contrasena

  #Este caso de prueba se enfocará en que los datos sean correctos
  Scenario: Restablecer contrasena con exito
          
    #Requerimiento: 
    Given cambiar la contrasena con el correo "cristiano_r@email.com", la nueva contrasena "nueva12" 
    y el token de la sesion iniciada "token"
     #Acción
     When tengo un token de restablecimiento válido para el correo electrónico "cristiano_r@email.com"
     #Condicion extra
     And el tiempo del token no ha expirado
     #Resultado esperado
     Then la respuesta debería tener un código de estado 200
     And debería recibir un mensaje que dice "Contraseña actualizada exitosamente"


  #Este caso de prueba se enfocará en que el token ya ha expirado
  Scenario: Iniciar sesion con las credenciales invalidas
          
    #Requerimiento: 
    Given cambiar la contrasena con el correo "cristiano_r@email.com", la nueva contrasena "nueva12" 
    y el token de la sesion iniciada "token"
     #Acción
     When tengo un token de restablecimiento válido para el correo electrónico "cristiano_r@email.com"
     #Condicion extra
     And el tiempo del token ha expirado
     #Resultado esperado
     Then la respuesta debería tener un código de estado 400
     And debería recibir un mensaje que dice "Token de recuperación inválido o expirado"

  #Este caso de prueba se enfocará en que el token de restablecimiento no existe o datos incorrectos
    Scenario: Iniciar sesion con las credenciales invalidas
            
    #Requerimiento: 
    Given cambiar la contrasena con el correo "cristiano_r@email.com", la nueva contrasena "nueva12" 
     y el token de la sesion iniciada "token"
     #Acción
     When tengo un token de restablecimiento invalido para el correo electrónico "cristiano_r@email.com"
     #Condicion extra
     And no tengo un token
     #Resultado esperado
     Then la respuesta debería tener un código de estado 400
     And debería recibir un mensaje que dice "No se encontró el token de recuperación"
