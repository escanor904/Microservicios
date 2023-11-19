Feature: Eliminación de usuarios

    #Este caso de prueba se enfocará en que las credenciales son validas
    Scenario: Obtener los datos del usuario con una sesion correcta

        #Requerimientos:
        Given tener usuario en una sesion
            #Acción
            When hacer la solicitud al servidor que elimine el usuario
            #Resultado esperado
            Then le muestra el mensaje que retorna el server "Usuario eliminado exitosamente    status code:200"

    #Este caso se basa en que se haya seleccionado un usuario con id no es valida
    Scenario: Obtener los datos del usuario con una sesion incorrecta

        #Requerimientos:
        Given no tener usuario en sesion
            #Acción
            When hacer la solicitud al servidor que elimine el usuario
            #Resultado esperado
            Then le muestra el mensaje que retorna el server "Usuario no encontrado     status code:400"