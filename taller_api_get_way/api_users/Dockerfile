FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN apt install libpq5
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir flask psycopg2 jsonschema Flask-JWT-Extended requests

EXPOSE 5000

CMD [ "python", "productor.py" ]