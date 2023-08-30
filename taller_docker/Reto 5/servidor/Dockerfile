FROM python:3.9

# Crea un usuario no root
RUN pip3 install --upgrade pip

# Establece el directorio de trabajo
WORKDIR /home/appuser/app

# Copia los archivos necesarios (app.py, etc.)
COPY servidor.py .

RUN pip3 install pyjwt


# Ejecuta el servidor
CMD ["python", "servidor.py"]

