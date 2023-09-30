from confluent_kafka import Consumer, KafkaError, KafkaException
import  sys
from config_consumidor import consumer_conf


# Configuración del consumidor de Kafka

consumer = Consumer(consumer_conf)
# Suscribe al mismo tema que el productor
topics = ["autenticacion-topic"]





def consume_loop(consumer,topics):
    try:
       #consumer.subscribe(topics)
       running= True
    
       while running:
           msg = consumer.poll(timeout=1.0)
           if msg is None: continue

           if msg.error():
               if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                   sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
               elif msg.error():
                       raise KafkaException(msg.error())
           else:
            
              msg_process(msg)
            
  
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
        

def msg_process(msg):
    try:
        # Decodificar el valor del mensaje como cadena UTF-8 (puedes ajustar la codificación según tus necesidades)
        message_value = msg.value().decode('utf-8')
        
        # Imprimir el contenido del mensaje en la consola
        print(f"Mensaje recibido en el tópico '{msg.topic()}': {message_value}")
        
    except Exception as e:
        print(f"Error al procesar el mensaje: {str(e)}")


consume_loop(consumer,topics)




