# models/usuario.py
from base_datos.conexion import Conexion

class Usuario:
    def __init__(self, nombre, password, isAdmin):
        self.nombre = nombre
        self.password = password
        self.isAdmin = isAdmin

    def guardar_en_db(self):
        conexion = Conexion('base_datos/feria_del_plato.db')
        result = conexion.agregar_usuario(self.nombre, self.password, self.isAdmin)
        conexion.cerrar_conexion()
        return result
