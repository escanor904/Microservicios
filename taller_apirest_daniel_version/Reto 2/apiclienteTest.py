import mysql.connector
import os

conexion = mysql.connector.connect(

    user="root" , password="Heropro.12",
    host="localhost",
    database="biblioteca",
    port="3306",
    
)

miCursor = conexion.cursor()
miCursor.execute("SHOW DATABASES")
consulta = miCursor.fetchall()

print(consulta)


