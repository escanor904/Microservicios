Feature: actualización de usuarios

    #Este caso de prueba se enfocará en que las credenciales son validas
    Scenario: Obtener los datos del usuario con una id valida

        #Requerimientos:
        Given tener un usuario en una sesion
        And tener un correo valido
            #Acción
            When hacer la solicitud al servidor que actualice el correo
            #Resultado esperado
            Then se muestra el mensaje que retorna el server "Usuario actualizada exitosamente    status code:200"

    #Este caso se basa en que se haya seleccionado un usuario con id no es valida
    Scenario: Obtener los datos del usuario con una id invalidas

        #Requerimientos:
        Given no tener un usuario en sesion
        And tener un correo no valido
            #Acción
            When hacer la solicitud al servidor que actualice el correo
            #Resultado esperado
            Then se muestra el mensaje que retorna el server "error     status code:400"