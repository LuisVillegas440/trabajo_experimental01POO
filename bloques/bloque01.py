# 1. Identifica 5 clases para modelar un sistema de biblioteca.
from utils import ValidationMixin, pedir_formulario
class BloqueUno(ValidationMixin):
    
    def ejercicio01(self):
        print("Identifica 5 nombre de clases.")
        campos = []
        for contador in range(5):
            campos.append({
                "nombre": f"clase_{contador}",
                "etiqueta": f"Clase {contador + 1}",
                "validacion": self.validar_campo,
                "campo": f"nombre de la clase {contador + 1}"
            })

        datos = pedir_formulario("CLASES DE BIBLIOTECA", campos)
        nombres = [datos[f"clase_{contador}"] for contador in range(5)]
        print(nombres)

    def ejercicio02(self):
        print("Ejercicio 2: Definir una clase Persona y crear 3 objetos diferentes.")
        class Persona:

            def __init__(self, nombre, edad):
                self.__nombre = nombre
                self.__edad = edad

            @property
            def nombre(self):
                return self.__nombre
            
            @property
            def edad(self):
                return self.__edad
            
            def info(self):
                return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
            
        persona1 = Persona("Juan", 30)
        persona2 = Persona("Maria", 25)
        persona3 = Persona("Carlos", 40)
        print(persona1.info())
        print(persona2.info())
        print(persona3.info())

        
    def ejercicio03(self):
        print("Explicar con tus propias palabras la diferencia entre una clase y un objeto.")
        print("Una clase es un molde o plantilla que define las características y comportamientos que tendrán los objetos de ese tipo.")
        print("Un objeto es una instancia específica de una clase, que tiene sus propios valores para las características definidas en la clase.")
