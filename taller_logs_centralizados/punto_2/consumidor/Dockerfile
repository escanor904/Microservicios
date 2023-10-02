FROM python:3.11

WORKDIR /app
#guarda todos los archivos de la carpeta app
COPY  app/ /app/  

RUN pip install kafka-python

CMD ["python", "consumidor.py"]


# FROM python:3.11

# # Crea un usuario no root
# RUN useradd -ms /bin/bash escanor
# USER escanor
# EXPOSE 80

# # Establece el directorio de trabajo
# WORKDIR /home/appuser/app

# # Copia los archivos necesarios (app.py, etc.)
# COPY cliente.py .

# # Ejecuta el servidor
# CMD ["python", "cliente.py"]