import os, time

class ConsumerConfig:
    SECRET_KEY ='mypass'
    time.sleep(20)
    KAFKA_TOPIC_NAME = os.environ['KAFKA_TOPIC_NAME']
    KAFKA_SERVER = os.environ['KAFKA_SERVER']
    KAFKA_PORT = os.environ['KAFKA_PORT']
    
    db_config = {
        # Configuración de la base de datos
        'dbname': os.environ['DB_NAME'],
        'user': os.environ['DB_USER'],
        'password': os.environ['POSTGRES_PASSWORD'],
        'host': os.environ['DATABASE_HOST'],
        'port': os.environ['DATABASE_PORT']
    }