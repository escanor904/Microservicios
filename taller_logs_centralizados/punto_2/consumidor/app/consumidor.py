# from confluent_kafka import Producer, Consumer, KafkaError
# import os
# # Configuración del productor o consumidor
# conf = {
#     'bootstrap.servers': os.environ['localhost:9092'],  # Cambia esto según la dirección de tu clúster Kafka
#     'group.id': 'mi_grupo',  # Solo se requiere para consumidores
#     'auto.offset.reset': 'earliest'  # Solo se requiere para consumidores
# }



# # Configuración del consumidor
# consumer = Consumer(conf)

# # Suscribirse a un tema
# topic = os.environ['KAFKA_SERVER=kafka']
# consumer.subscribe([topic])

# while True:
#     msg = consumer.poll(1.0)

#     if msg is None:
#         continue

#     if msg.error():
#         if msg.error().code() == KafkaError._PARTITION_EOF:
#             print('Llegó al final de la partición')
#         else:
#             print('Error en el mensaje: {}'.format(msg.error()))
#     else:
#         print('Mensaje recibido: key={}, value={}'.format(msg.key(), msg.value()))

# from confluent_kafka import Consumer, KafkaError
# import json

# class KafkaConsumer:
#     def __init__(self, bootstrap_servers, group_id, auto_offset_reset='earliest'):
#         self.consumer = Consumer({
#             'bootstrap.servers': bootstrap_servers,
#             'group.id': group_id,
#             'auto.offset.reset': auto_offset_reset
#         })

#     def consume_messages(self, topic):
#         self.consumer.subscribe([topic])

#         while True:
#             msg = self.consumer.poll(1.0)

#             if msg is None:
#                 continue
#             if msg.error():
#                 if msg.error().code() == KafkaError._PARTITION_EOF:
#                     continue
#                 else:
#                     print(f"Error al consumir mensaje: {msg.error()}")
#                     continue

#             # Procesar el mensaje (en este ejemplo, simplemente lo imprimimos)
#             message_value = msg.value()
#             if message_value:
#                 try:
#                     # Si el mensaje está en formato JSON, lo cargamos como diccionario
#                     message_value = json.loads(message_value)
#                 except json.JSONDecodeError:
#                     pass
#                 print(f"Mensaje recibido en el topic '{msg.topic()}' --> {message_value}")

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
