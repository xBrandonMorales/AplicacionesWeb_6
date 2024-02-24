import web

urls = (
    '/lista_productos', 'ListaProductos',
    '/ver_producto', 'VerProducto',
    '/insertar_producto', 'InsertarProducto',
    '/borrar_producto', 'BorrarProducto',
    '/actualizar_producto', 'ActualizarProducto',
)

# Define la variable render antes de las clases
render = web.template.render('mvc/views/')

class ListaProductos:
    def GET(self):
        return render.lista_productos()

class VerProducto:
    def GET(self):
        return render.ver_producto()

class InsertarProducto:
    def GET(self):
        return render.insertar_producto()

class BorrarProducto:
    def GET(self):
        return render.borrar_producto()

class ActualizarProducto:
    def GET(self):
        return render.actualizar_producto()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
