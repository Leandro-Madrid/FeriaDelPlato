# models/producto.py
from base_datos.conexion import Conexion

class Producto:
    def __init__(self, nombre, descripcion, stock, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio

    def guardar_en_db(self):
        conexion = Conexion('base_datos/feria_del_plato.db')
        result = conexion.agregar_producto(self.nombre, self.descripcion, self.stock, self.precio)
        conexion.cerrar_conexion()
        return result
