import web
"""Importamos la clase ModeloContactos del modelo modelo_contactos.py"""
from mvc.models.modelo_contactos import ModeloContactos

render = web.template.render('mvc/views/', base='layout')

m_contactos = ModeloContactos() # Se crea objeto de la clase Modelo Contactos

class Contactos:
    def GET(self):
        try:
            resultado = m_contactos.consultaContactos()
            return render.contactos(resultado)
        except Exception as e:
            print(f"Error 101 - contactos {e.args}")
            return "Ups algo salio mal"
