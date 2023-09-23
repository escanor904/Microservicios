from confluent_kafka import Producer, Consumer, KafkaError
import os
# Configuración del productor o consumidor
conf = {
    'bootstrap.servers': os.environ['KAFKA_SERVER=kafka'],  # Cambia esto según la dirección de tu clúster Kafka
    'group.id': 'mi_grupo',  # Solo se requiere para consumidores
    'auto.offset.reset': 'earliest'  # Solo se requiere para consumidores
}



# Configuración del consumidor
consumer = Consumer(conf)

# Suscribirse a un tema
topic = os.environ['KAFKA_SERVER=kafka']
consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Llegó al final de la partición')
        else:
            print('Error en el mensaje: {}'.format(msg.error()))
    else:
        print('Mensaje recibido: key={}, value={}'.format(msg.key(), msg.value()))
