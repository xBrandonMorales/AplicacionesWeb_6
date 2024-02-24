import web
import mysql.connector

class ModeloContactos:
    def __init__(self):
        pass

    def consultaContactos(self):

        conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="contactos"
            )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT nombres, apellidos, telefono FROM contactos")

        # Obtener los resultados
        datos = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()
        """datos = [
            ("Erick", "Pérez", "1234567890"),
            ("Carlos", "González", "9876543210"),
            ("Jair", "Martínez", "5551234567"),
            ("Cesar", "Sánchez", "7778889990")
        ]"""
        return datos  # regresa la lista de tuplas
