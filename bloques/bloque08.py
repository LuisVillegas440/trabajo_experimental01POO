class BloqueOcho:
    def ejercicio01(self):
        print("Función que calcule el doble de un número.")
        def calcular_doble(*numero):
            dobles = [x * 2 for x in numero]
            return dobles
        
        numeros = [1, 3, 5, 7, 9]
        
        print(f"El doble de estos números: {numeros} es: {calcular_doble(*numeros)}")

    def ejercicio02(self):
        def sumar_numeros(*numeros):
            suma = sum(numeros)
            return suma
        
        print(f"La suma de los números 1, 2, 3, 4, 5 es: {sumar_numeros(1, 2, 3, 4, 5)}")
    
    def ejercicio03(self):
        print("Función recursiva para calcular el factorial de n.")
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        print(f"Factorial de 5: {factorial(5)}")