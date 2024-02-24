import web
"""Importamos la clase ModeloIndex del modelo modelo_index.py"""
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

m_index = ModeloIndex() # Se crea objeto de la clase Modelo Index

class Index:
    def GET(self):
        try:
            resultado = m_index.consultaIndex()
            return render.index(resultado)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Ups algo salio mal"
