class Venta:
    def __init__(self, id, productos_vendidos, vendedor, precio_total):
        self.id = id
        self.productos_vendidos = productos_vendidos
        self.vendedor = vendedor
        self.precio_total = precio_total

    @staticmethod
    def realizar_venta(productos_vendidos, vendedor):
        precio_total = sum(item.precio for item in productos_vendidos)
        # Registrar la venta
        for item in productos_vendidos:
            item.actualizar_stock(1)  # Suponiendo que vendemos solo 1 unidad por producto
        return Venta(generar_id(), productos_vendidos, vendedor, precio_total)

    @staticmethod
    def obtener_ventas_totales(ventas):
        return sum(venta.precio_total for venta in ventas)

    @staticmethod
    def filtrar_por_vendedor(ventas, vendedor):
        return [venta for venta in ventas if venta.vendedor == vendedor]
