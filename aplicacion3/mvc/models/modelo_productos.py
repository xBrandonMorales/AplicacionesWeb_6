import web
import mysql.connector
class ModeloProductos:
    def __init__(self):
        pass

    def consultaProductos(self):
        conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="contactos"
            )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT nombre, precio, cantidad FROM productos")

        # Obtener los resultados
        datos = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()
        """datos = [
            ("Laptop HP", 800, 10),  # Producto, Precio, Cantidad
            ("Mouse Logitech", 30, 50),
            ("Tableta 7''", 200, 20),
            ("Hub USB c", 15, 30)
        ]"""
        return datos  # regresa la lista de tuplas
