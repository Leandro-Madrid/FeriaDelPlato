import sqlite3

class Conexion:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self._conexion = None

    # Obtiene la conexión a la base de datos si no está establecida.
    def obtener_conexion(self):
        if self._conexion is None:
            self._conexion = sqlite3.connect(self.nombre_bd)
        return self._conexion

    # Propiedad que devuelve la conexión a la base de datos.
    @property
    def conexion(self):
        return self.obtener_conexion()

    # Obtiene un cursor para ejecutar consultas en la base de datos.
    def obtener_cursor(self):
        return self.conexion.cursor()

    # Cierra la conexión a la base de datos.
    def cerrar_conexion(self, exception=None):
        conexion = self._conexion
        if conexion is not None:
            conexion.close()
            self._conexion = None

    # Crea la tabla 'usuarios' si no existe.
    def crear_tabla_usuarios(self):
        cursor = self.obtener_cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, password TEXT NOT NULL, isAdmin INTEGER DEFAULT 0)")
        self.conexion.commit()

    # Crea la tabla 'productos' si no existe.
    def crear_tabla_productos(self):
        cursor = self.obtener_cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT, stock INTEGER NOT NULL, precio FLOAT NOT NULL)")
        self.conexion.commit()

    # Inserta un nuevo usuario en la base de datos.
    def agregar_usuario(self, nombre, password, isAdmin=0):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("INSERT INTO usuarios (nombre, password, isAdmin) VALUES (?, ?, ?)", (nombre, password, isAdmin))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # Inserta un nuevo producto en la base de datos.
    def agregar_producto(self, nombre, descripcion, stock, precio):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("INSERT INTO productos (nombre, descripcion, stock, precio) VALUES (?, ?, ?, ?)", (nombre, descripcion, stock, precio))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # Actualiza un usuario existente en la base de datos.
    def actualizar_usuario(self, usuario_id, nombre, isAdmin):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("UPDATE usuarios SET nombre = ?, isAdmin = ? WHERE id = ?", (nombre, isAdmin, usuario_id))
            self.conexion.commit()
            return True
        except sqlite3.Error:
            return False

    # Elimina un usuario de la base de datos.
    def borrar_usuario(self, usuario_id):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
            self.conexion.commit()
            return True
        except sqlite3.Error:
            return False

    # Actualiza un producto existente en la base de datos.
    def actualizar_producto(self, producto_id, nombre, descripcion, stock, precio):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, stock = ?, precio = ? WHERE id = ?", (nombre, descripcion, stock, precio, producto_id))
            self.conexion.commit()
            return True
        except sqlite3.Error:
            return False

    # Elimina un producto de la base de datos.
    def borrar_producto(self, producto_id):
        try:
            cursor = self.obtener_cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            self.conexion.commit()
            return True
        except sqlite3.Error:
            return False

    # Obtiene todos los usuarios de la base de datos.
    def mostrar_usuarios(self):
        cursor = self.obtener_cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        return usuarios

    # Obtiene todos los productos de la base de datos.
    def mostrar_productos(self):
        cursor = self.obtener_cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return productos

    # Obtiene un usuario por su ID de la base de datos.
    def obtener_usuario_por_id(self, usuario_id):
        cursor = self.obtener_cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
        usuario = cursor.fetchone()
        return usuario

    # Obtiene un producto por su ID de la base de datos.
    def obtener_producto_por_id(self, producto_id):
        cursor = self.obtener_cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()
        return producto
