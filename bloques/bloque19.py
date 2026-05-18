from utils import ValidationMixin, pedir_formulario
from model import ProductoDescuento


class BloqueDiecinueve(ValidationMixin):

    def ejercicio01(self):
        datos_producto = pedir_formulario("DATOS DEL PRODUCTO", [
            {"nombre": "nombre", "etiqueta": "Nombre del producto", "validacion": self.validar_str, "campo": "nombre"},
            {"nombre": "precio", "etiqueta": "Precio", "validacion": self.validar_numero_float, "campo": "precio"},
            {"nombre": "descuento", "etiqueta": "Descuento (%)", "validacion": self.validar_descuento, "campo": "descuento"}
        ])

        nombre = datos_producto["nombre"]
        precio = datos_producto["precio"]
        descuento = datos_producto["descuento"]

        producto = ProductoDescuento(nombre, precio, descuento)

        print(producto.info())
