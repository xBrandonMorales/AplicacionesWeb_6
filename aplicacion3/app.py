"""Framewerk web.py"""
import web

#  Rutas de los controladores
urls = (
    '/', 'mvc.controllers.index.Index',
    '/contactos', 'mvc.controllers.contactos.Contactos',
    '/productos', 'mvc.controllers.productos.Productos'
)

app = web.application(urls, globals())

#  Punto de entrada
if __name__ == "__main__":
    web.config.debug = False
    app.run()
    