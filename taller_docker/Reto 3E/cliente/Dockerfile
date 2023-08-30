# Definir la imagen base
FROM alpine:3.10

# Actualizar la lista de paquetes e instalar los paquetes necesarios
RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip

# Copiamos el codigo server al directorio del contenedor
COPY cliente.py /home

# Ejecutar el servidor cuando el contenedor se inicie
CMD ["python3", "home/cliente.py"]