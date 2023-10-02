import os, time


class ConsumerConfig:
    SECRET_KEY ='mypass'
    time.sleep(20)
    KAFKA_TOPIC_NAME = os.environ['KAFKA_TOPIC_NAME']
    KAFKA_SERVER = os.environ['KAFKA_SERVER']
    KAFKA_PORT = os.environ['KAFKA_PORT']
    

