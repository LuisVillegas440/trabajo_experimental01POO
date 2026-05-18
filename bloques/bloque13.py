from utils import ValidationMixin, pedir_formulario

class BloqueTrece(ValidationMixin):
    def ejercicio01(self):
        print("===Captura el ValueError al convertir input del usuario a int.===\n")
        try:
            datos = pedir_formulario("CONVERTIR A ENTERO", [
                {"nombre": "numero", "etiqueta": "Numero", "validacion": self.validar_numero_entero, "campo": "numero"}
            ])
            numero = datos["numero"]
            print(f"Has introducido el número: {numero}")
        except ValueError:
            print("Error: No has introducido un número válido. Por favor, intenta de nuevo.")

    def ejercicio02(self):
        print("===Captura IndexError al acceder lista[5] en una lista de 3 elementos.===\n") 
        try:
            lista = [1, 2, 3]
            print(f"El elemento en la posición 5 es: {lista[5]}")
        except IndexError:
            print("Error: Índice fuera de rango. Por favor, intenta de nuevo.")

    def ejercicio03(self):
        print("===Escribe un try/except que maneje tanto ValueError como ZeroDivisionError.===\n")
        try:
            datos = pedir_formulario("DIVISION", [
                {"nombre": "numerador", "etiqueta": "Numerador", "validacion": self.validar_numero_entero, "campo": "numerador"},
                {"nombre": "denominador", "etiqueta": "Denominador", "validacion": self.validar_numero_denominador, "campo": "denominador"}
            ])
            numerador = datos["numerador"]
            denominador = datos["denominador"]
            resultado = numerador / denominador
            print(f"El resultado de {numerador} / {denominador} es: {resultado}")
        except ValueError:
            print("Error: No has introducido un número válido. Por favor, intenta de nuevo.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Por favor, intenta de nuevo.")
