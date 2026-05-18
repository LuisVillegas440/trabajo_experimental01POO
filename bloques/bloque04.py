class BloqueCuatro:
    
    def ejercicio01(self):
        print("===Con a=20, b=4 imprime todos los operadores aritméticos y sus resultados.===")
        a = 20
        b = 4
        print(f"Suma: {a} + {b} = {a + b}")
        print(f"Resta: {a} - {b} = {a - b}")
        print(f"Multiplicación: {a} * {b} = {a * b}")
        print(f"División: {a} / {b} = {a / b}")
        print(f"División entera: {a} // {b} = {a // b}")
        print(f"Módulo: {a} % {b} = {a % b}")
        print(f"Exponente: {a} ** {b} = {a ** b}")

    def ejercicio02(self):
        print("===Crea dos listas idénticas y demuestra que == es True pero is es False.===")
        lista1 = [1, 2, 3]
        lista2 = [1, 2, 3]
        print(f"lista1 == lista2: {lista1 == lista2}")
        print(f"lista1 is lista2: {lista1 is lista2}")

    def ejercicio03(self):
        print("===Evalúa: x = 2 + 1 * 2 % 2 + (2**1)//2 → explica el orden de evaluación.===")
        
        x = 2 + 1 * 2 % 2 + (2**1)//2
        print(f"Resultado de la expresión: {x}")
        print("Orden de evaluación:")
        print("1. Paréntesis: (2**1) se evalúa primero, resultando en 2.")
        print("2. Exponentes: 2**1 se evalúa, resultando en 2.")
        print("3. Multiplicación y módulo: 1 * 2 se evalúa, resultando en 2, luego 2 % 2 se evalúa, resultando en 0.")
        print("4. División entera: (2**1)//2 se evalúa, resultando en 1.")
        print("5. Suma: Finalmente, se suman los resultados: 2 + 0 + 1, resultando en 3.")