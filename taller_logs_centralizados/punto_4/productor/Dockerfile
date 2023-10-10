FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN apt install libpq5
RUN pip install -r requirements.txt

CMD [ "python", "productor.py" ]