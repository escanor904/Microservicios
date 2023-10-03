from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de almacenamiento de logs en una lista
logs = []

# Definición de la estructura de un log
class Log:
    def __init__(self, application, log_type, module, timestamp, summary, description):
        self.application = application
        self.log_type = log_type
        self.module = module
        self.timestamp = timestamp
        self.summary = summary
        self.description = description

# Ruta para obtener todos los logs con filtros y paginación
@app.route('/logs', methods=['GET'])
def get_logs():
    # Obtener parámetros de consulta
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    log_type = request.args.get('log_type')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Filtrar logs por fecha y tipo de log
    filtered_logs = logs
    if start_date:
        # Realiza el filtrado por rango de fechas si se proporciona
        filtered_logs = [log for log in filtered_logs if log.timestamp >= start_date]
    if end_date:
        filtered_logs = [log for log in filtered_logs if log.timestamp <= end_date]
    if log_type:
        filtered_logs = [log for log in filtered_logs if log.log_type == log_type]

    # Paginación
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_logs = filtered_logs[start_index:end_index]

    # Convertir logs a formato JSON
    logs_json = [log.__dict__ for log in paginated_logs]

    return jsonify(logs_json)

# Ruta para obtener logs de una aplicación específica con filtros y paginación
@app.route('/logs/<application>', methods=['GET'])
def get_logs_by_application(application):
    # Obtener parámetros de consulta
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    log_type = request.args.get('log_type')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Filtrar logs por aplicación, fecha y tipo de log
    filtered_logs = [log for log in logs if log.application == application]
    if start_date:
        filtered_logs = [log for log in filtered_logs if log.timestamp >= start_date]
    if end_date:
        filtered_logs = [log for log in filtered_logs if log.timestamp <= end_date]
    if log_type:
        filtered_logs = [log for log in filtered_logs if log.log_type == log_type]

    # Paginación
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_logs = filtered_logs[start_index:end_index]

    # Convertir logs a formato JSON
    logs_json = [log.__dict__ for log in paginated_logs]

    return jsonify(logs_json)

# Ruta para crear un nuevo log
@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    application = data['application']    #Aplicacion que manda a crear el log
    log_type = data['log_type']     #Tipo de log (error, advertencia, informacion)
    module = data['module']    #Funciones, variables u otros elementos de código que se ejecutaron
    timestamp = data['timestamp']       #Fecha y hora en la que se genero el log
    summary = data['summary']       #Mensaje general del error
    description = data['description']       #Descripcion mas detallada del error

    new_log = Log(application, log_type, module, timestamp, summary, description)
    logs.append(new_log)

    return jsonify({'message': 'Log created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)