FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask psycopg2 jsonschema Flask-JWT-Extended requests

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]