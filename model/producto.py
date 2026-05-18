class ProductoDescuento:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def calcular_precio_final(self):
        rebaja = self.precio * self.descuento / 100
        precio_final = self.precio - rebaja
        return precio_final

    def info(self):
        return f"Producto: {self.nombre} | Precio final: ${self.calcular_precio_final():.2f}"