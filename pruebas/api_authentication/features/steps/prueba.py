import jwt

# Datos a incluir en el token (en este caso, solo la dirección de correo electrónico)
email = "cristiano_r@email.com"

# Clave secreta para firmar el token (cambia esto por tu propia clave)
clave_secreta = "mypass"

# Crear el token JWT
token = jwt.encode({"email": email}, clave_secreta, algorithm="HS256")

print("Token JWT:", token)

try:
    # Decodificar el token JWT utilizando la clave secreta
    decoded_token = jwt.decode(token, clave_secreta, algorithms=["HS256"])
    # Recuperar la información del token (en este caso, la dirección de correo electrónico)
    email = decoded_token.get("email")
    print("Dirección de correo electrónico recuperada:", email)
except jwt.ExpiredSignatureError:
    print("El token ha expirado.")
except jwt.InvalidTokenError:
    print("Token no válido o firma incorrecta.")