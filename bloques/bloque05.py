
from utils import ValidationMixin, pedir_formulario

class BloqueCinco(ValidationMixin):
    def ejercicio01(self):
        print("Solicita nombre y edad; muestra un mensaje personalizado con f-string. ")
        class Persona():
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad

        datos = pedir_formulario("DATOS DE PERSONA", [
            {"nombre": "nombre", "etiqueta": "Nombre", "validacion": self.validar_str, "campo": "nombre"},
            {"nombre": "edad", "etiqueta": "Edad", "validacion": self.validar_numero_entero, "campo": "edad"}
        ])

        persona = Persona(datos["nombre"], datos["edad"])
        print(f"Hola {persona.nombre}, tienes {persona.edad} años.")

    def ejercicio02(self):
        print("Lee dos números, calcúla su suma y promedio, e imprímelos. ")
        def calcular_suma_y_promedio(num1, num2):
            suma = num1 + num2
            promedio = suma / 2
            return suma, promedio   
        
        suma, promedio = calcular_suma_y_promedio(10, 20)
        print(f"Suma: {suma}, Promedio: {promedio}")

    def ejercicio03(self):
        print("Sin convertir el input, imprime el resultado de número + '5'. ¿Qué pasa?")
        datos = pedir_formulario("CONCATENAR INPUT", [
            {"nombre": "numero", "etiqueta": "Numero", "validacion": self.validar_campo, "campo": "numero"}
        ])
        numero = datos["numero"]
        resultado = numero + "5"
        print(type(resultado))
        print(f"Resultado de número + '5': {resultado}")
