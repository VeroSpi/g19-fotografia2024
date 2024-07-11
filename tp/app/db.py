# pip install pymysql

# conectar a la base de datos:
 

import pymysql

# Configurar la conexión a la base de datos
user = "root"
password = ""
host = "localhost"
database = "fotografia"

def conexionMySQL():
    return pymysql.connect(user=user, host=host, password=password, database=database)
