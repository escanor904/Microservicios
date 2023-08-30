import socket
import jwt
import pickle

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al puerto
server_address = ('0.0.0.0', 80)
# * desempaqueta la dupla
print('iniciando en  {} port {}'.format(*server_address))
# Escuche las conexiones entrantes
sock.bind(server_address)
#(1) es la cantidad de conexiones que se pueden establecer
sock.listen(1)

while True:
    # espera por una conexion
    print('esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print('conectado a', client_address)

        # Recibir los datos en pequeños fragmentos y retransmitirlos
        while True:
            data = connection.recv(160)
            print('recibido {!r}'.format(data))
            if data:
                print('enviando los datos de vuelta a el cliente')
                diccionario = pickle.loads(data)
                
                
                
                id = diccionario["ID"]
                nombre = diccionario["NOMBRE"]
                secreto = diccionario["SECRETO"]
                                
                print (id)
                
                token = jwt.encode(
                    {'id':id,'nombre':nombre},
                    secreto,
                    algorithm='HS256'
                )
                
                
                
                print(token)
                
                respuesta = (token).encode('utf-8')
                connection.sendall(respuesta)
            else:
                print('no se recibieron datos de', client_address)
                break

    finally:
        # cerrar la conexion
        connection.close()
        
        

