import os
import time

class DevelopmentConfig:
    SECRET_KEY ='mypass'
    time.sleep(20)
   
    


db_config = {
    # Configuración de la base de datos
    'dbname': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': os.environ['DATABASE_HOST'],
    'port': os.environ['DATABASE_PORT']
}

KAFKA_SERVER = os.environ['KAFKA_SERVER']
KAFKA_PORT = os.environ['KAFKA_PORT']
confluent_config = {
    
    'bootstrap.servers': f'{KAFKA_SERVER}:{KAFKA_PORT}',  # Dirección de los brokers de Kafka
    'client.id': 'python-producer'
}
