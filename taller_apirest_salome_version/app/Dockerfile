# app/Dockerfile
FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]