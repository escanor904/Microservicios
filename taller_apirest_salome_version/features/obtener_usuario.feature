Feature: Obtencion de usuarios

    $Este caso se basa en que se haya seleccionado un usuario con id valida
    Scenario: Obtener los datos del usuario con una id valida

        #Requerimiento:
        Given obtener la informacion del usuario existente
            #Acción
            When se verifica el id
            #Resultado esperado
            Then mostrar el mensaje del servidor "{user}"

    #Este caso se basa en que se haya seleccionado un usuario con id no es valida
    Scenario: Obtener los datos del usuario con una id invalidas

        #Requerimiento:
        Given obtener la informacion del usuario no existente
            #Acción
            When se verifica el id
            #Resultado esperado
            Then mostrar el mensaje del servidor "err   505"