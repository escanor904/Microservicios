FROM python:3.9

RUN pip3 install --upgrade pip

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios (app.py, etc.)
COPY apicliente.py .

RUN pip3 install mysql-connector-python


# Ejecuta el servidor
CMD ["python", "apicliente.py"]


