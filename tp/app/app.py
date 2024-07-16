#  .venv\Scripts\activate
# cd app --> flask --app app 
# run --debug

from flask import Flask, render_template, request, redirect, url_for
from controller_db import *

app = Flask(__name__)

# Sección Inicio
@app.route("/")
def Inicio():
    title = "Inicio"
    return render_template("index.html", titulo=title)

# @app.route("/contactosagendados/<int:id>")
# def datacontactos(id):
#     title="Reservas"
#     return render_template("contactosagendados.html",title=title,contactos=contactos[id])


# Sección Contacto
@app.route("/contacto")
def Contacto():
    contacto = ver_contactos()
    title = "contacto"
    return render_template("contacto.html", title=title, 
    contacto=contacto)

# Insert
# cargar el contacto
@app.route("/cargar_contacto")
def agregar_contacto():
    title= "Cargar Contacto"
    return render_template("nuevo_contacto.html", title=title)

# enviar el  formulario de contacto por el metodo post
@app.route("/guardar_contacto", methods=["POST"])
def guardar_contacto():
    title= "Guardar Contacto"
    print(request.form)
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    fecha_evento = request.form["fecha_evento"]
    cargar_contacto(nombre, apellido,email,telefono,fecha_evento)
    return  redirect("/contacto")

# update 
@app.route("/editar_contacto/<int:id>")
def editar_contacto(id):
    title = "Editar contacto"
    contacto_por_id = obtener_contacto_por_id(id)
    return render_template("editar_contacto.html", title=title, contacto=contacto_por_id)

# @app.route("/editar_contacto", methods=["GET","POST"])
# def guardar_edicion_contacto():
#     id_edit = request.form["id"]
#     nombre = request.form["nombre"]
#     apellido = request.form["apellido"]
#     email = request.form["email"]
#     telefono = request.form["telefono"]
#     fecha_evento = request.form["fecha_evento"]
#     resp = actualizar_contacto(id_edit,nombre, apellido,email,telefono,fecha_evento)
#     return  redirect("/contacto")

@app.route("/editar_contacto", methods=["POST"])
def guardar_edicion_contacto():
    id = request.form.get("id")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    fecha_evento = request.form.get("fecha_evento")

    actualizar_contacto(id, nombre, apellido, email, telefono, fecha_evento)
    return redirect("/contacto")
    
# delete
@app.route("/borrar_contacto/<int:id>")
def delte_contacto(id):
    eliminar_contacto(id)
    return redirect("/contacto")


# Sección Conóceme
@app.route("/conoceme")
def conoceme():
    title = "conoceme"
    return render_template("conoceme.html", titulo=title)

# Sección Galería
@app.route("/galeria")
def galeria():
    title = "galeria"
    return render_template("galeria.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)




