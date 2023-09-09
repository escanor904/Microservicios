Feature: Listado de usuarios paginados

  #Este caso de prueba se enfocará en que los datos sean correctos
  Scenario: Listar usuarios paginados exitosamente
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When proporcionar parametros de paginacion "1" y tamaño "2"
     #Resultado esperado
     Then se recibe una respuesta con "Código de estado 200"
     And la respuesta contiene una lista de 2 usuarios 


  #Este caso de prueba se enfocará en que los datos sean correctos
  Scenario: Listar usuarios sin parametros de paginacion
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When proporcionar los parametros de paginacion "" y tamaño ""
     #Resultado esperado
     Then se recibe una respuesta con "Código de estado 400"
     And la respuesta contiene una lista de 2 usuarios 


 #Este caso de prueba se enfocará en que los datos sean correctos
  Scenario: Listar usuarios con paginacion inválida
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     #Acción
     When proporcionar los parametros de paginacion "1" y tamaño "-2"
     #Resultado esperado
     Then se recibe una respuesta con "Código de estado 400"
     And la respuesta contiene una lista de "Paginacion invalida"


  #Este caso de prueba se enfocará en el error sea del servidor
  Scenario: Error en el servidor al listar usuarios
          
    #Requerimiento: 
    Given establecer la conexion con la base de datos
     And se simula un error en el servidor
     #Acción
     When obtener los parametros de paginacion "1" y tamaño "2"
     #Resultado esperado
     Then se recibe una respuesta con código de estado 500
     And la respuesta contiene el mensaje "Error en el servidor"

 