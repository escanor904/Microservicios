# app/Dockerfile
FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --force-reinstall psycopg2
RUN apt-get install libpq-dev

COPY . .

CMD [ "python", "app.py" ]