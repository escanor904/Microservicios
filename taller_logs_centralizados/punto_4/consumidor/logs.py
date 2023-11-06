import logging
from json import loads
from config_consumidor import  ConsumerConfig
from kafka import KafkaConsumer
import os
import csv
import psycopg2, json,  logging

def consumer_loop():
    try:
        # Configuración del consumidor de Kafka
        consumer = KafkaConsumer(
            ConsumerConfig.KAFKA_TOPIC_NAME,
            bootstrap_servers=f'{ConsumerConfig.KAFKA_SERVER}:{ConsumerConfig.KAFKA_PORT}',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
        )

       
    
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

        for message in consumer:
            # Extraer valores del mensaje de Kafka
            event_type = message.value.get('event_type')
            user_email = message.value.get('user_email')
            timestamp = message.value.get('timestamp')

             # Establecer una conexión con la base de datos PostgreSQL
            conn = psycopg2.connect(**ConsumerConfig.db_config)
            cursor = conn.cursor()
            # Ejecutar una consulta SQL para insertar los datos del usuario en la tabla 'users'
            cursor.execute("INSERT INTO logs (evento, user_email, fecha_log) VALUES (%s, %s, %s)",
                       (event_type, user_email, timestamp))

            # Confirmar la transacción y cerrar el cursor y la conexión
            conn.commit()
            cursor.close()
            conn.close() 

            # # Escribir los valores en el archivo CSV
            # with open(csv_filename, mode='a', newline='') as csv_file:
            #     fieldnames = ['event_type', 'user_email', 'timestamp']
            #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #     writer.writerow({'event_type': event_type, 'user_email': user_email, 'timestamp': timestamp})
            
            logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.info("Guardado en logs: event_type=%s, user_email=%s, timestamp=%s" % (event_type, user_email, timestamp))

    except Exception as e:
        logging.error('Error en el bucle del consumidor', e)

if __name__ == '__main__':
    consumer_loop()



# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     consumer_loop()
#     app.run(debug=True)



# -----------------------------------------LOGS TEST---------------------------
# Ruta para obtener todos los logs con filtros y paginación
# @app.route('/logs', methods=['GET'])
# def get_logs():
#     # Obtener parámetros de consulta
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     log_type = request.args.get('log_type')
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 10))

#     # Leer los logs del archivo CSV
#     logs = []
#     with open(csv_filename, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             logs.append(row)

#     # Filtrar logs por fecha y tipo de log
#     filtered_logs = logs
#     if start_date:
#         filtered_logs = [log for log in filtered_logs if log['timestamp'] >= start_date]
#     if end_date:
#         filtered_logs = [log for log in filtered_logs if log['timestamp'] <= end_date]
#     if log_type:
#         filtered_logs = [log for log in filtered_logs if log['log_type'] == log_type]

#     # Paginación
#     start_index = (page - 1) * per_page
#     end_index = start_index + per_page
#     paginated_logs = filtered_logs[start_index:end_index]

#     return jsonify(paginated_logs)

# # Ruta para obtener logs de una aplicación específica con filtros y paginación
# @app.route('/logs/<application>', methods=['GET'])
# def get_logs_by_application(application):
#     # Obtener parámetros de consulta
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     log_type = request.args.get('log_type')
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 10))

#     # Leer los logs del archivo CSV
#     logs = []
#     with open(csv_filename, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             logs.append(row)

#     # Filtrar logs por aplicación, fecha y tipo de log
#     filtered_logs = [log for log in logs if log['application'] == application]
#     if start_date:
#         filtered_logs = [log for log in filtered_logs if log['timestamp'] >= start_date]
#     if end_date:
#         filtered_logs = [log for log in filtered_logs if log['timestamp'] <= end_date]
#     if log_type:
#         filtered_logs = [log for log in filtered_logs if log['log_type'] == log_type]

#     # Paginación
#     start_index = (page - 1) * per_page
#     end_index = start_index + per_page
#     paginated_logs = filtered_logs[start_index:end_index]

#     return jsonify(paginated_logs)

# # Ruta para crear un nuevo log
# @app.route('/logs', methods=['POST'])
# def create_log():
#     data = request.get_json()
#     application = data['application']       #Aplicacion que manda a crear el log
#     log_type = data['log_type']             #Tipo de log (error, advertencia, informacion)
#     module = data['module']                 #Funciones, variables u otros elementos de código que se ejecutaron
#     timestamp = data['timestamp']           #Fecha y hora en la que se genero el log
#     summary = data['summary']               #Mensaje general del error
#     description = data['description']       #Descripcion mas detallada del error

#     # Escribir el nuevo log en el archivo CSV
#     with open(csv_filename, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([application, log_type, module, timestamp, summary, description])

#     return jsonify({'message': 'Log created successfully'}), 201

# if __name__ == '__main__':
#     app.run(debug=True)
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     print("corre")
#     consumer_loop()
