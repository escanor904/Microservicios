# Definir la imagen base
FROM alpine:3.10

# Actualizar la lista de paquetes e instalar los paquetes necesarios
RUN apk update && \
    apk add --no-cache python3-dev libffi-dev gcc musl-dev linux-headers && \
    pip3 install --upgrade pip

# Copiamos el código server al directorio del contenedor
COPY . /home

# Instalamos módulos necesarios para JWT
RUN pip3 --no-cache-dir install cffi pyjwt

# Ejecutar el servidor cuando el contenedor se inicie
CMD ["python3", "/home/servidor.py"]
