FROM python:3

# Copiar el archivo.py que queremos ejecutar a la imagen.
COPY servidor.py /
#Esto no realiza la publicación del puerto en el host, pero indica la intención de que el contenedor acepte conexiones en el puerto 80.
#EXPOSE 80
# Ejecutar el archivo al iniciar la imagen en un contenedor.
CMD ["python", "./servidor.py"]


