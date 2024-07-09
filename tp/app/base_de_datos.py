# pip install pymysql

# conectar a la base de datos:
#  

import pymysql

# Configurar la conexión a la base de datos
user = "root"
password = ""
host = "localhost"
database = "fotografia"

def conexionMySQL():
    connection = pymysql.connect(user=user, host=host, password=password, database=database)


# def conexionMySQL():
#     try:
#         connection = pymysql.connect(user=user, host=host, password=password, database=database)
#         print("Conexión exitosa")
#         return connection
#     except pymysql.MySQLError as e:
#         print(f"Error al conectar a la base de datos: {e}")
#         return None


# @app.route('/bd-contactos')
# def contactos():
#     title = contactos
#     conn = mysql.conexion.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM contactos")
#     contactos = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return render_template('contactos.html', title = title)
