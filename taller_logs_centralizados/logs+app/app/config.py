import os
class DevelopmentConfig:
    SECRET_KEY ='mypass'


db_config = {
    # Configuración de la base de datos
    'dbname': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': os.environ['DATABASE_HOST'],
    'port': os.environ['DATABASE_PORT']
}
