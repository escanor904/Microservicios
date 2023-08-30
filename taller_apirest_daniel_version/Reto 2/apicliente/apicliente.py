import mysql.connector
import os
import time
print("conectando al servidor ip:"+os.environ['SERVIDOR_DIRECCION'])
time.sleep(20)
conexion = mysql.connector.connect(

    user="root", password="root",
    host=os.environ['SERVIDOR_DIRECCION'],
    database="bd_usuarios",
    port="3306",
    
)

miCursor = conexion.cursor()
miCursor.execute("SHOW DATABASES")
consulta = miCursor.fetchall()

print(consulta)


