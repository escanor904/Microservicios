import psycopg2,  logging, threading
from json import loads
from config_consumidor import  ConsumerConfig
from kafka import KafkaConsumer
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Lista en memoria para almacenar registros de logs
logs = []

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

        # muestra el log en la consola
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

        for message in consumer:
            # Extraer valores del mensaje de Kafka
            nombre_app = message.value.get('nombre_app')
            log_type = message.value.get('log_type')
            descripcion = message.value.get('descripcion')

             # Establecer una conexión con la base de datos PostgreSQL
            conn = psycopg2.connect(**ConsumerConfig.db_config)
            cursor = conn.cursor()
            # Ejecutar una consulta SQL para insertar los datos del usuario en la tabla 'users'
            cursor.execute("INSERT INTO logs (nombre_app, tipo_log, descripcion) VALUES (%s, %s, %s)",
                           (nombre_app, log_type, descripcion))

            # Confirmar la transacción y cerrar el cursor y la conexión
            conn.commit()
            cursor.close()
            conn.close() 
 
            logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.info("Guardado en logs: aplication=%s, log_type=%s, descripcion=%s" % (nombre_app, log_type, descripcion))

    except Exception as e:
        logging.error('Error en el bucle del consumidor', e)

#-------------------------------------Logs-----------------------------------------------------------------------------------------
@app.route('/logs', methods=['GET'])
def get_logs():
    # Obtener parámetros de consulta
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    log_type = request.args.get('log_type')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Establecer una conexión con la base de datos PostgreSQL
    conn = psycopg2.connect(**ConsumerConfig.db_config)
    cursor = conn.cursor()

    # Construir la consulta SQL para obtener los logs filtrados
    sql_query = "SELECT * FROM logs WHERE 1=1"
    params = []

    if start_date:
        sql_query += " AND fecha_log >= %s"
        params.append(start_date)
    if end_date:
        sql_query += " AND fecha_log <= %s"
        params.append(end_date)
    if log_type:
        sql_query += " AND tipo_log = %s"
        params.append(log_type)

    sql_query += " ORDER BY fecha_log ASC"

    # Ejecutar la consulta SQL
    cursor.execute(sql_query, tuple(params))
    result = cursor.fetchall()

    # Paginación
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_logs = result[start_index:end_index]

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return jsonify(paginated_logs)

# Ruta para obtener logs de una aplicación específica con filtros y paginación
@app.route('/logs/<application>', methods=['GET'])
def get_logs_by_application(application):
    # Obtener parámetros de consulta
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    log_type = request.args.get('log_type')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Establecer una conexión con la base de datos PostgreSQL
    conn = psycopg2.connect(**ConsumerConfig.db_config)
    cursor = conn.cursor()

    # Construir la consulta SQL para obtener los logs filtrados por aplicación
    sql_query = "SELECT * FROM logs WHERE nombre_app = %s"
    params = [application]

    if start_date:
        sql_query += " AND fecha_log >= %s"
        params.append(start_date)
    if end_date:
        sql_query += " AND fecha_log <= %s"
        params.append(end_date)
    if log_type:
        sql_query += " AND tipo_log = %s"
        params.append(log_type)

    sql_query += " ORDER BY fecha_log ASC"

    # Ejecutar la consulta SQL
    cursor.execute(sql_query, tuple(params))
    result = cursor.fetchall()

    # Paginación
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_logs = result[start_index:end_index]

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # Verificar si no hay registros para la aplicación especificada
    if not result:
        abort(400, f"No se encontraron registros para la aplicación '{application}'")

    return jsonify(paginated_logs)


# Ruta para crear un nuevo log
@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    if not data or 'application' not in data or 'log_type' not in data or 'description' not in data:
        return jsonify({'message': 'Datos faltantes'}), 400  # Si faltan datos, retorna un código 400
    application = data['application']       #Aplicacion que manda a crear el log
    log_type = data['log_type']             #Tipo de log (error, advertencia, informacion)         #Fecha y hora en la que se genero el log
    description = data['description']       #Descripcion mas detallada del error
    
    # Establecer una conexión con la base de datos PostgreSQL
    conn = psycopg2.connect(**ConsumerConfig.db_config)
    cursor = conn.cursor()
    # Ejecutar una consulta SQL para insertar los datos del usuario en la tabla 'logs'
    cursor.execute("INSERT INTO logs (nombre_app, tipo_log, descripcion) VALUES (%s, %s, %s)",
                   (application, log_type, description))
    
    # Confirmar la transacción y cerrar el cursor y la conexión
    conn.commit()
    cursor.close()
    conn.close() 
   
    return jsonify({'message': 'Log creado exitosamente'}), 201

#---------------------------Rutas salud------------------
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'message': 'Health check OK'})

@app.route('/health/ready', methods=['GET'])
def health_ready():
    database_ready = verificar_conexion_bd
    kafka_ready = verificar_kafka

    if database_ready and kafka_ready:
        return jsonify({'status': 'Ready'})
    else:
        return jsonify({'status': 'Not Ready'}), 503  # Devuelve un código de estado 503 si no está listo

@app.route('/health/live', methods=['GET'])
def health_live():
    return jsonify({'message': 'Live'})

def verificar_conexion_bd():
    try:
        # Establecer conexión con la base de datos PostgreSQL
        conn= psycopg2.connect(**ConsumerConfig.db_config)
      
        # Verificar si la conexión se ha establecido correctamente
        if conn:
            print("Conexión exitosa a la base de datos PostgreSQL.")
            conn.close()
            return True

    except psycopg2.OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False

def verificar_kafka():
    try:
        consumer_loop.send(ConsumerConfig.KAFKA_TOPIC_NAME, value={"test": "message"})
        return True
    except Exception as e:
        print(f"Error al conectar a Kafka: {e}")
        return False

if __name__ == '__main__':
    hiloconsumer = threading.Thread(target=consumer_loop)
    hiloconsumer.start()
    app.run(debug=True, host='0.0.0.0', port=8081)
    
