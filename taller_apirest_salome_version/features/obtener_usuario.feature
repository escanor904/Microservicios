Feature: Obtencion de usuarios

    $Este caso se basa en que se haya seleccionado un usuario con id valida
    Scenario: Obtener los datos del usuario con una id valida

        #Requerimiento:
        Given establecer la conexion DB
        And obtener la informacion del usuario
            #Acción
            When el id es de un usuario existente
            #Condicion extra
            And envio su id
            #Resultado esperado
            Then recibo la informacion del usuario

    #Este caso se basa en que se haya seleccionado un usuario con id no es valida
    Scenario: Obtener los datos del usuario con una id invalidas

        #Requerimiento:
        Given establecer la conexion DB
        And obtener mensaje de usuario no valido
            #Acción
            When el id del usuario no es valido
            #Condicion extra
            And envio su id
            #Resultado esperado
            Then se muestra el mensaje de "Usuario no valido"