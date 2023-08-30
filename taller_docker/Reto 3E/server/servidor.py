from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import jwt
import datetime
import os

# Clave secreta para firmar el JWT (asegúrate de manejarla de manera segura)
clave_secreta = 'clave_secreta_super_segura'

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write("Servidor en funcionamiento.".encode('utf-8'))
        return

    def do_POST(self):
        # Leer el contenido de la solicitud POST recibe el
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        msj = 'Hola '+post_data
        # Parsear la información recibida
        #parsed_data = urllib.parse.parse_qs(post_data)
        # nombre_usuario = parsed_data.get('nombre', [''])[0] 

        # Configurar la respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Generar un JWT con los datos del usuario (nombre) como payload
        if os.path.getsize(post_data)>0:
            # Crear la carga útil (payload) del JWT

            
            # Generar el JWT
            #jwt_token = jwt.encode(datos_usuario, clave_secreta, algorithm='HS256')
            self.wfile.write(msj.encode('utf-8'))
        else:
            self.wfile.write("Error: No se proporcionó un nombre de usuario.".encode('utf-8'))
        return

def main():
    host = "0.0.0.0"
    port = 80

    # Configurar el servidor con el manejador personalizado
    server = HTTPServer((host, port), MyRequestHandler)
    print(f"Servidor esperando en el puerto {port}...")

    # Mantener el servidor en ejecución
    server.serve_forever()

if __name__ == "__main__":
    main()
