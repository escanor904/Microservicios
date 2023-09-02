Feature: Inicio de Sesión en una Aplicación

  Scenario: Iniciar sesión con credenciales válidas
    Given que estoy en la página de inicio de sesión
    When ingreso mi nombre de usuario "usuario123" y contraseña "contraseña123"
    And presiono el botón de inicio de sesión
    Then debería estar en la página de inicio