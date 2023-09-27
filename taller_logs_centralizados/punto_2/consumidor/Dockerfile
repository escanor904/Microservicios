FROM python:3.11

WORKDIR /app

COPY app/consumidor.py consumidor.py

RUN pip install confluent-kafka

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