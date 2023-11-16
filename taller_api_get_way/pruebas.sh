#!/bin/bash

# Función para verificar el estado de la respuesta
verificar_estado() {
    response="$1"
    # Extraer el código de estado de la salida de curl
    status=$(echo "$response" | tail -n1)
    
    if [ "$status" = "200" ]; then
        echo "Solicitud exitosa (Código de estado: $status)"
    else
        echo "Error en la solicitud (Código de estado: $status)"
    fi
}

# Prueba de inicio de sesión exitoso

echo "Probando inicio de sesión exitoso..."

# Realizar la solicitud POST al endpoint de inicio de sesión del microservicio
login_success=$(curl -s -w "%{http_code}\n" -X POST -H "Content-Type: application/json" -d '{"email": "isaac_n@email.com", "password": "16"}' http://127.0.0.1:5001/inicio_sesion)

# Mostrar la respuesta de la solicitud de inicio de sesión
echo "Respuesta de inicio de sesión:"
response_login="${login_success%$'\n'*}" # Obtener la respuesta sin el código de estado
echo "$response_login"
verificar_estado "$login_success"
echo ""

# Prueba de registro de usuario

echo "Probando registro de usuario..."

# Realizar la solicitud POST al endpoint de registro del microservicio
registro_usuario=$(curl -s -w "%{http_code}\n" -X POST -H "Content-Type: application/json" -d '{"username": "nuev_usuario", "password": "22", "email": "newSer@email.com"}' http://127.0.0.1:5001/registro)

# Mostrar la respuesta de la solicitud de registro de usuario
echo "Respuesta de registro de usuario:"
response_registro="${registro_usuario%$'\n'*}" # Obtener la respuesta sin el código de estado
echo "$response_registro"
verificar_estado "$registro_usuario"
