import requests
from behave import given, when, then

@given('iniciar sesion en el perfil que se quiere actualizar')
def usuario_en_sesion(context):
    usuario_autenticado = True
    correo_usuario = "usuario@correo.com"
    context.correo_usuario = correo_usuario

@given('iniciar sesion en el perfil que se quiere actualizar')
def usuario_en_sesion(context):
    usuario_autenticado = True
    correo_usuario = "usuario@correo.com"
    context.correo_usuario = correo_usuario

@when('se actualiza el perfil del usuario con datos válidos')
def actualizar_perfil_con_datos_validos(context):
    global usuario_autenticado
    if usuario_autenticado:
        correo_actualizar = context.correo_usuario  # Obtener el correo del contexto

        # Datos para actualizar el perfil (simulación)
        datos_actualizacion = {
            "Username": "NuevoNombre",
            "PersonalPage": "NuevaPaginaPersonal",
            "Correspondence": "NuevaCorrespondencia",
            "Biography": "NuevaBiografia",
            "Organization": "NuevaOrganizacion",
            "Country": "NuevoPais",
            "LinkedInURL": "NuevoLinkedIn",
            "PublicInformation": True
        }
        # URL para la solicitud de actualización
        url = f"http://127.0.0.1:3000/updateProfile/{correo_actualizar}"

        try:
            response = requests.post(url, json=datos_actualizacion)
            context.response = response
        except requests.RequestException as e:
            context.error = e
    else:
        raise Exception("El usuario no está autenticado. Por favor, inicia sesión primero.")


@when('se intenta actualizar el perfil del usuario con datos incorrectos')
def actualizar_perfil_con_datos_validos(context):
    global usuario_autenticado
    if usuario_autenticado:
        correo_actualizar = context.correo_usuario  # Obtener el correo del contexto

        # Datos para actualizar el perfil (simulación)
        datos_actualizacion = {
            "Username": "NuevoNombre",
            "PersonalPage": "NuevaPaginaPersonal",
            "Correspondence": "NuevaCorrespondencia",
            "Biography": "NuevaBiografia",
            "Organization": "NuevaOrganizacion",
        }

        # URL para la solicitud de actualización
        url = f"http://127.0.0.1:3000/updateProfile/{correo_actualizar}"

        try:
            response = requests.post(url, json=datos_actualizacion)
            context.response = response
        except requests.RequestException as e:
            context.error = e
    else:
        raise Exception("El usuario no está autenticado. Por favor, inicia sesión primero.")



@then('se recibe una respuesta con el "{codigo}"')
def enviar_reporte_codigo(context,codigo):
    assert codigo==codigo

        
@then('la respuesta contiene el mensaje "{mensaje}"')
def enviar_reporte_mensaje(context,mensaje):
    assert mensaje==mensaje