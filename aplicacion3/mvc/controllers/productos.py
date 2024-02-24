import web
"""Importamos la clase ModeloProductos del modelo modelo_productos.py"""
from mvc.models.modelo_productos import ModeloProductos

render = web.template.render('mvc/views/', base='layout')

m_contactos = ModeloProductos() # Se crea objeto de la clase Modelo Index

class Productos:
    def GET(self):
        try:
            resultado = m_contactos.consultaProductos()
            return render.productos(resultado)
        except Exception as e:
            print(f"Error 101 - productos {e.args}")
            return "Ups algo salio mal"
