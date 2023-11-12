import psycopg2, json,  logging
import datetime
from flask import Flask, request, jsonify
from config_consumidor import ConsumerConfig

app = Flask(__name__)

# Lista en memoria para almacenar registros de logs
logs = []

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

    return jsonify(paginated_logs)


# Ruta para crear un nuevo log
@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    application = data['application']       #Aplicacion que manda a crear el log
    log_type = data['log_type']             #Tipo de log (error, advertencia, informacion)
    timestamp = data['timestamp']           #Fecha y hora en la que se genero el log
    description = data['description']       #Descripcion mas detallada del error
    user_email = data['email']
    
    # Establecer una conexión con la base de datos PostgreSQL
    conn = psycopg2.connect(**ConsumerConfig.db_config)
    cursor = conn.cursor()
    # Ejecutar una consulta SQL para insertar los datos del usuario en la tabla 'logs'
    cursor.execute("INSERT INTO logs (nombre_app, tipo_log, fecha_log, descripcion, user_email) VALUES (%s, %s, %s, %s, %s)",
                   (application, log_type, timestamp, description,user_email))
    
    # Confirmar la transacción y cerrar el cursor y la conexión
    conn.commit()
    cursor.close()
    conn.close() 
   
    return jsonify({'message': 'Log creado exitosamente'}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
