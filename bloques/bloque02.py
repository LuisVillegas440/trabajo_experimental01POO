from utils import ValidationMixin

class BloqueDos:


    def ejercicio01(self):
        print("Crea la clase Producto con código, nombre y precio. Instancia 2 productos.")
        class Producto:
            def __init__(self, codigo, nombre, precio):
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                self.codigo = codigo
                self.nombre = nombre
                self.precio = precio

            def __str__(self):
                return f"Producto: {self.nombre}, Código: {self.codigo}, Precio: ${self.precio}"
            

                

        producto1 = Producto("P001", "Laptop", 1500)
        producto2 = Producto("P002", "Smartphone", 90)
        print(producto1)
        print(producto2)

    def ejercicio02(self):
        print("Crea Estudiante con nombre y notas=None. Si no hay notas, inicia lista vacía.")
        
        class Estudiante:
            def __init__(self, nombre, nota=None):
                
                self.nombre = nombre
                
                if nota is None:
                     self.notas = []
                else:
                    self.notas = nota
                

            def __str__(self):
                return f"Estudiante: {self.nombre}, Nota: {self.notas}"
            
            #Diccionario a objeto
            @classmethod
            def from_dict(cls, data):
                return cls(data["nombre"], 
                           data["notas"])
            

        estudiante01 = Estudiante("Ana")
        estudiante02 = Estudiante("Luis", 100)
        print(estudiante01)
        print(estudiante02)

        datos_estudiante = {"nombre": "Luis", "notas": [88, 92, 95]}
        estudiante03 = Estudiante.from_dict(datos_estudiante)
        print(estudiante03)
