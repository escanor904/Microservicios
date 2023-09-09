Feature: Restablecimiento de contrasena

  #Este caso de prueba se enfocará en que los datos sean correctos
  Scenario: Restablecer contrasena con exito
          
    #Requerimiento: 
    Given el usuario se encuentra ya registrado
     #Acción
     When el usuario proporciona el token, el correo electrónico y una nueva contraseña
     #Condicion extra
     And hacer la solicitud al servidor que actualice la contrasena
     #Resultado esperado
     Then la respuesta debería tener un "código de estado 200"
     And se captura el mensaje de respuesta "Contraseña actualizada exitosamente"


  #Este caso de prueba se enfocará en que el token ya ha expirado
  Scenario: Iniciar sesion con las credenciales invalidas
          
    #Requerimiento: 
    Given el usuario se encuentra ya registrado
     #Acción
     When el usuario proporciona un token expirado, el correo electrónico y una nueva contraseña
     #Condicion extra
     And hacer la solicitud al servidor que actualice la contrasena
     #Resultado esperado
     Then la respuesta debería tener un código de estado 400
     And debería recibir un mensaje que dice "Token de recuperación expirado"

  #Este caso de prueba se enfocará en que el token de restablecimiento no existe o datos incorrectos
    Scenario: Iniciar sesion con las credenciales invalidas o el token no existe
            
    #Requerimiento: 
    Given el usuario se encuentra ya registrado
     #Acción
     When el usuario proporciona un token que no existe, el correo electrónico y una nueva contraseña
     #Condicion extra
     And hacer la solicitud al servidor que actualice la contrasena
     #Resultado esperado
     Then la respuesta debería tener un código de estado 400
     And debería recibir un mensaje que dice "No se encontró el token de recuperación o los datos son invalidos"
