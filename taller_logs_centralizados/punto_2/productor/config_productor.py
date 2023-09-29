class DevelopmentConfig:
    SECRET_KEY ='mypass'


db_config = {
    # Configuración de la base de datos
    'dbname': 'authentication_db',
    'user': 'admin',
    'password': 'admin_password',
    'host': 'localhost'
}

confluent_config = {
    'bootstrap.servers': 'localhost:29092',  # Dirección de los brokers de Kafka
    'client.id': 'python-producer'
}
