FROM python:3.11

WORKDIR /app
#guarda todos los archivos de la carpeta app
COPY  . /app/  

# RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev

RUN pip install psycopg2-binary
RUN apt install libpq5

RUN pip install kafka-python
RUN pip install Flask

RUN pip install --no-cache-dir Flask psycopg2-binary jsonlogging Flask-Limiter Flask-Caching Flask-Bcrypt Flask-JWT-Extended requests
RUN apt-get update && apt-get install -y postgresql-client

EXPOSE 8081

CMD ["python", "logs.py"]

