Feature: Creacion de un nuevo log

  Scenario: Crear un nuevo log con datos válidos
    # Requerimiento:
    Given un usuario realice alguna accion en el sistema
    #Acción
    When se realiza una solicitud con los datos del nuevo log
    # Resultado esperado
    Then se crea el log exitosamente y retorna un mensaje de éxito con el "código de estado 201"

  Scenario: Crear un nuevo log sin proporcionar algunos datos obligatorios
    # Requerimiento: 
    Given un usuario realice alguna accion en el sistema
    # Acción
    When se realiza una solicitud sin proporcionar ciertos datos obligatorios del nuevo log
    # Resultado esperado
    Then se retorna un mensaje de error indicando datos faltantes con el "código de estado 400"