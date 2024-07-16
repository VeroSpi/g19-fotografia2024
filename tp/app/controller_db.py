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
    
# create -> INSERT
def cargar_contacto(nombre, apellido,email,telefono,fecha_evento):
    # conexion:
    conexion = conexionMySQL()
    # consulta db:
    with conexion.cursor() as cursor:
        # Read a single record
        sql = "INSERT INTO contactos (nombre, apellido,email,telefono,fecha_evento) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(nombre, apellido,email,telefono,fecha_evento))

        #  se procesan los resultados:
        result = cursor.lastrowid
        # cerrar la conexion:
        conexion.commit()
        conexion.close()
        return result
    
# update -> 1)
def obtener_contacto_por_id(id):
    # conexion:
    conexion = conexionMySQL()
    # consulta db:
    with conexion.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM contactos WHERE id = %s"
        cursor.execute(sql,(id))
        #  se procesan los resultados:
        result = cursor.fetchone()

        # cerrar la conexion:
    conexion.commit()
    conexion.close()
    return result

# update -> 2)
def actualizar_contacto(nombre, apellido,email,telefono,fecha_evento,id):
    # conexion:
    conexion = conexionMySQL()
    # consulta db:
    with conexion.cursor() as cursor:
        # consulta de acltualizacion
        cursor.execute("UPDATE contactos SET nombre = %s, apellido = %s, email = %s, telefono = %s, fecha_evento = %s WHERE id = %s",(nombre, apellido, email, telefono, fecha_evento, id))
        #  se procesan los resultados:
        result = cursor
        # cerrar la conexion:
        conexion.commit()
        conexion.close()
        return result
    
# borrar -> delete 
def eliminar_contacto(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM contactos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result
