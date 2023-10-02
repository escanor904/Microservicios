import logging
from json import loads
from config_consumidor import ConsumerConfig
from kafka import KafkaConsumer 



def consumer_loop():
    try:
        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(
            ConsumerConfig.KAFKA_TOPIC_NAME,
            bootstrap_servers=f'{ConsumerConfig.KAFKA_SERVER}:{ConsumerConfig.KAFKA_PORT}',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
        )
        
        for message in consumer:
            logging.basicConfig(level=logging.INFO,  # Establece el nivel de registro (puedes usar 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Define el formato del mensaje de registro
            
            logger = logging.getLogger(__name__)
            
            logger.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))

    except Exception as e:
        logging.info('Connection successful', e)



consumer_loop()




