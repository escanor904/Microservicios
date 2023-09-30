import os, time


class ConsumerConfig:
    SECRET_KEY ='mypass'
    time.sleep(20)
   

KAFKA_SERVER = os.environ['KAFKA_SERVER']
KAFKA_PORT = os.environ['KAFKA_PORT']
consumer_conf = {
    'bootstrap.servers': f'{KAFKA_SERVER}:{KAFKA_PORT}',  # Dirección de los brokers de Kafka
    'group.id': 'mi_grupo',
    'auto.offset.reset': 'earliest'
}
