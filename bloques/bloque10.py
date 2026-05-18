class BloqueDiez:
    def ejercicio01(self):
        print("Crea una tupla con 4 elementos. Intenta modificar el primero y observa el error. ")
        tupla = (1, 2, 3, 4)
        print(f"Tupla original: {tupla}")
        try:
            tupla[0] = 10
        except TypeError as e:
            print(f"Error al intentar modificar la tupla: {e}")
        print("Las tuplas son inmutables, por lo que no se pueden modificar después de su creación. Para modificar una tupla, se debe crear una nueva tupla con los valores deseados.")

    def ejercicio02(self):
        print("Usa unpacking para asignar los valores (100,200,300,400) → a, b, *resto.")
        a, b, *resto = (100, 200, 300, 400)
        print(f"a: {a}, b: {b}, resto: {resto}")

    def ejercicio03(self):
        print("Recorre una lista de coordenadas (tuplas) con for e imprime x e y. ")
        coordenadas = [(1, 2), (3, 4), (5, 6)]
        for x, y in coordenadas:
            print(f"Coordenada: ({x}, {y})")