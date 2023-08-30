import http.client
import time

def send_data(nombre):
    # Definir la información de la solicitud
    host = "servidor"  # El nombre del servicio definido en el archivo docker-compose.yml
    port = 80
    path = "/"

    # Crear los datos para enviar como cuerpo de la solicitud
    data = "nombre=" + nombre

    # Configurar las cabeceras de la solicitud
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": len(data)
    }

    # Realizar la solicitud HTTP POST al servidor
    conn = http.client.HTTPConnection(host, port)
    conn.request("POST", path, data, headers)
    response = conn.getresponse()

    # Leer y decodificar la respuesta del servidor
    server_response = response.read().decode('utf-8')
    conn.close()

    return server_response

def main():
    # Esperar unos segundos para que el servidor esté listo
    time.sleep(5)  # Espera 5 segundos antes de intentar comunicarse con el servidor
    
    # Enviar el nombre al servidor y obtener la respuesta
    nombre = "sebas"  # Cambia esto al nombre que desees enviar al servidor
    respuesta = send_data(nombre)

    # Imprimir la respuesta del servidor
    print("Respuesta del servidor:", respuesta)

if __name__ == "__main__":
    main()
