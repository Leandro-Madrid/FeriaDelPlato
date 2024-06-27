class Informe:
    @staticmethod
    def generar_informe_ventas_totales(ventas):
        return sum(venta.precio_total for venta in ventas)

    @staticmethod
    def generar_informe_productos_mas_vendidos(ventas):
        # Implementación para generar el informe de productos más vendidos
        pass

    @staticmethod
    def generar_informe_combos_mas_vendidos(ventas):
        # Implementación para generar el informe de combos más vendidos
        pass
