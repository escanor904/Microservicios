from behave import given, when, then, step

@given('cambiar la contraseña con el correo "{email}" y la nueva contraseña "{new_password} "y el token de la sesion iniciada " {token}')
def obtener_restablecimiento_contra(context, email, new_password, token):
    context.email = email
    context.new_password = new_password
    context.token = token

@when('tengo un token de restablecimiento válido para el correo electrónico "{email}"')
def verficiar_token_email(context, email):
    context.reset_token = reset_token

@then('la respuesta debería tener un código de estado 200')
def respuesta_exitosa(context):
    response_json = context.response.json()
    assert context.response.status_code == 200
    assert response_json["mensaje"] == "Contraseña actualizada exitosamente"
