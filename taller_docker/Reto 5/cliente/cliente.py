import socket
import pickle
import os

# Datos para construir el JWS
idUsuario = os.environ['ID_USUARIO']
nombre=  os.environ['NOMBRE']



mi_diccionario = {
    "SECRETO": "123",
    "ID": idUsuario,
    "NOMBRE": nombre
}

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
direccion_server = os.environ['SERVIDOR_DIRECCION']

# Conecte el socket al puerto donde el servidor está escuchando
server_address = (direccion_server, 80)
print('conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:

    # enviar data
    
    message = pickle.dumps(mi_diccionario)
    
   # print('enviando {!r}'.format(message))
    sock.sendall(message)

    # busca la respuesta
    cantidad_recibida = 0
    #cantidad_esperada = len(message)

    while cantidad_recibida == 0:
        data = sock.recv(160)
        cantidad_recibida += len(data)
        print('recibido {!r}'.format(data))

finally:
    print('cerrando el socket')
    sock.close()