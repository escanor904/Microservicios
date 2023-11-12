FROM python:3.8


COPY . /.

RUN pip install --no-cache-dir Flask psycopg2-binary jsonlogging Flask-Limiter Flask-Caching Flask-Bcrypt Flask-JWT-Extended requests

RUN apt-get update && apt-get install -y postgresql-client

EXPOSE 8081

ENV NAME World

CMD ["python", "logs.py"]