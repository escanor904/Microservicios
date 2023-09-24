# import logging
# from json import loads

# from app.enum import EnvironmentVariables as EnvVariables

# from kafka import KafkaConsumer


# def main():
#     try:
#         # Para consumir los mensajes más recientes y confirmar automáticamente las compensaciones
#         consumer = KafkaConsumer(
#             EnvVariables.KAFKA_TOPIC_NAME.get_env(),
#             bootstrap_servers=f'{EnvVariables.KAFKA_SERVER.get_env()}:{EnvVariables.KAFKA_PORT.get_env()}',
#             value_deserializer=lambda x: loads(x.decode('utf-8')),
#             auto_offset_reset='earliest',
#             enable_auto_commit=True,
#         )
#         for message in consumer:
#             print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                                  message.offset, message.key, message.value))

#     except Exception as e:
#         logging.info('Connection successful', e)


from confluent_kafka import Producer, KafkaError
import json

# Configuración del productor Kafka
producer_conf = {
    # Cambia el servidor y puerto según tu configuración
    'bootstrap.servers': 'localhost:29092', 
}

producer = Producer(producer_conf)

# Función para serializar y enviar un mensaje cuando un usuario se autentica
def enviar_mensaje_autenticacion(email):
    mensaje = {
        'event_type': 'autenticacion',
        'user_email': email
    }
    
    # Serializar el mensaje como JSON
    mensaje_serializado = json.dumps(mensaje).encode('utf-8')
    
    # Enviar el mensaje al tema 'autenticacion-topic'
    producer.produce('autenticacion-topic', value=mensaje_serializado)
    
    # Esperar a que el mensaje se entregue (esto es opcional y puede omitirse si no es necesario)
    producer.flush()
    
    # Manejar cualquier error que pueda ocurrir al enviar
    while True:
        try:
            producer.poll(0)
            break
        except Exception as e:
            if isinstance(e, KafkaError) and e.args[0].code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error al enviar mensaje: {str(e)}")
                break

# Cerrar el productor al finalizar
producer.flush()  # Asegurar que todos los mensajes pendientes se entreguen antes de cerrar
producer = None  # Liberar el objeto productor
