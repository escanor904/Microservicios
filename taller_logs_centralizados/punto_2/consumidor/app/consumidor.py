from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor de Kafka
consumer_conf = {
    'bootstrap.servers': 'localhost:29092',  # Cambia esto según tu configuración de Kafka
    'group.id': 'mi_grupo',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
# Suscribe al mismo tema que el productor
print("sa")
consumer.subscribe(['autenticacion-topic'])
try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error(): 
            if msg.error().code() == '':
                print('Llegó al final de la partición')
            else:
                print('Error en el mensaje: {}'.format(msg.error()))
        else:
            mensaje = json.loads(msg.value())
            print('Mensaje recibido: event_type={}, user_email={}, timestamp={}'.format(
                mensaje['event_type'], mensaje['user_email'], mensaje['timestamp']
            ))

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
