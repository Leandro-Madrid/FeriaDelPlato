class Combo:
    def __init__(self, id, nombre, lista_productos, precio):
        self.id = id
        self.nombre = nombre
        self.lista_productos = lista_productos
        self.precio = precio

    @staticmethod
    def crear(admin, id, nombre, lista_productos, precio):
        if admin.is_admin:
            return Combo(id, nombre, lista_productos, precio)
        else:
            print("Solo los administradores pueden crear nuevos combos.")

    def modificar(self, admin, nombre=None, lista_productos=None, precio=None):
        if admin.is_admin:
            if nombre:
                self.nombre = nombre
            if lista_productos:
                self.lista_productos = lista_productos
            if precio:
                self.precio = precio
        else:
            print("Solo los administradores pueden modificar combos.")

    def borrar(self, admin):
        if admin.is_admin:
            del self
        else:
            print("Solo los administradores pueden borrar combos.")
