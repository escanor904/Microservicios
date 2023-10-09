FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev

COPY . .

EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN apt install libpq5
RUN pip install -r requirements.txt


CMD [ "python", "productor.py" ]



# FROM python:3.9

# # Crea un usuario no root
# RUN useradd -ms /bin/bash escanor
# USER escanor
 

# # Establece el directorio de trabajo
# WORKDIR /home/appuser/app

# # Copia los archivos necesarios (app.py, etc.)
# COPY cliente.py .

# # Ejecuta el servidor
# CMD ["python", "cliente.py"]
