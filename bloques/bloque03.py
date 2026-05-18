import os 
os.system("clear")

class BloqueTres:
    
    def ejercicio01(self):
        print("====Declara una variable de cada tipo simple y complejo e imprímelas.====")
        # Tipos simples
        entero = 42
        flotante = 3.14
        booleano = True
        cadena = "Hola, mundo!"
        vacio = None
        print("Tipos simples:")
        print(f"Entero: {entero}")
        print(f"Flotante: {flotante}")
        print(f"Booleano: {booleano}")
        print(f"Cadena: {cadena}")
        print(f"Vacío: {vacio}")
        print("\nTipos complejos:")
        # Tipos complejos
        lista = [1, 2, 3, 4, 5]
        tupla = (1, 2, 3)
        conjunto = {1, 2, 3}
        diccionario = {"clave1": "valor1", "clave2": "valor2"}
        print(f"Lista: {lista}")
        print(f"Tupla: {tupla}")
        print(f"Conjunto: {conjunto}")
        print(f"Diccionario: {diccionario}")

    def ejercicio02(self):
        print("====Crea una lista con 5 elementos. Imprime el primero, el último y lista[1:4].====")
        lista = [10, 20, 30, 40, 50]
        print(f"Lista completa: {lista}")
        print(f"Primer elemento: {lista[0]}")
        print(f"Último elemento: {lista[-1]}")
        print(f"Elementos de la posición 1 a 3: {lista[1:4]}")

    def ejercicio03(self):
        print("====Crea una clase con un método que declare un str, una list y un dict. ====")
        print("====Imprimir: primer carácter del texto, último elemento de la lista, valor de una clave del dict.====")
        class Metodo:
            def __init__(self):
                self.texto = "Hola, mundo!"
                self.lista = [10, 20, 30, 40, 50]
                self.diccionario = {"clave1": "valor1", "clave2": "valor2"}

            def imprimir_valores(self):
                print(f"De la palabra {self.texto} el primer carácter es: {self.texto[0]}")
                print(f"De la lista {self.lista} el último elemento es: {self.lista[-1]}")
                print(f"Del diccionario {self.diccionario} el valor de la clave 'clave1' es: {self.diccionario['clave1']}")

        metodo = Metodo()
        metodo.imprimir_valores()