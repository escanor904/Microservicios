from behave import given
import jwt  # Asegúrate de tener instalada la librería PyJWT

# Función para verificar si el token es válido
def verificar_token(token):
    try:
        # Decodificar y verificar el token utilizando una clave secreta (reemplaza 'tu_clave_secreta' por tu clave real)
        decoded_token = jwt.decode(token, 'tu_clave_secreta', algorithms=['HS256'])
        return True  # El token es válido
    except jwt.ExpiredSignatureError:
        return False  # El token ha expirado
    except jwt.InvalidTokenError:
        return False  # El token es inválido

# Paso Given para verificar que el usuario tiene un token válido
@given('que el usuario está en sesión con un token válido')
def usuario_en_sesion(context):
    # Supongamos que tienes acceso al token del usuario en tu contexto o variable de entorno
    token_usuario = context.token_acceso  # Reemplaza con la variable que contiene el token

    # Verificar si el token está vigente
    context.usuario_en_sesion = verificar_token(token_usuario)
