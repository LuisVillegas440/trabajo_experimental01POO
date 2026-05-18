class BloqueSiete:

    def ejercicio01(self):
        print("===Imprime los números del 1 al 10 utilizando un bucle while.===")
        contador = 1
        while contador <= 10:
            print(contador)
            contador += 1

    def ejercicio02(self):
        print("===Recorre una lista de frutas con enumerate() e imprime índice y nombre.===")
        frutas = ["manzana", "banana", "cereza", "durazno", "uva"]
        for index, fruta in enumerate(frutas):
            print(f"Índice: {index }, Fruta: {fruta}")

    def ejercicio03(self):
        print("===Calcula los cuadrados de los números pares del 1 al 10.===")
        cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0]
        print(f"Cuadrados pares del 1 al 10: {cuadrados}")