FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev

COPY . .

RUN pip install -r requirements.txt
RUN pip install --force-reinstall psycopg2

CMD [ "python", "productor.py" ]



# FROM python:3.9

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
