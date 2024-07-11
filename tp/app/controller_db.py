from db import conexionMySQL

# consultas -> CRUD

# read -> SELECT
def ver_contactos():
    # conexion:
    conexion = conexionMySQL()
    # consulta db:
    with conexion.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM contactos"
        cursor.execute(sql)
        #  se procesan los resultados:
        result = cursor.fetchall()

        # cerrar la conexion:
        conexion.commit()
        conexion.close()
        return result