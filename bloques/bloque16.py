from functools import reduce


class BloqueDieciseis:

    def ejercicio01(self):
        print("Usa map() para incrementar en 1 cada elemento de [2,4,6].")

        numeros = [2, 4, 6]
        print(f"Lista: {numeros}")

        aumentar = list(map(lambda x: x + 1, numeros))
        print(f"lista con 1 aumentando en cada elemento: {aumentar}")


    def ejercicio02(self):
        print("Usa filter() para obtener los mayores a 3 de [1,2,3,4,5].")

        numeros = [1, 2, 3, 4, 5]
        print(f"Lista: {numeros}")
        numeros_mayores = list(filter(lambda x: x > 3, numeros ))
        print(f"De la lista: {numeros} los mayores a 3 son :{numeros_mayores}")

    def ejercicio03(self):
        print("Usa reduce() para multiplicar todos los elementos de [1,2,3,4].")

        numeros = [1, 2, 3, 4]
        print(f"lista: {numeros}")
        multiplicar_numeros = reduce(lambda x, y: x * y, numeros)
        print(f"El resultado de multiplicar toda esta lista: {numeros} es : {multiplicar_numeros}")