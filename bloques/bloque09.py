class BloqueNueve:
    def ejercicio01(self):
        print("Crea lista, agrégale 3 elementos con append(), ordénala y muéstrala. ")
        lista = [5, 2, 9]
        lista.append(1)
        lista.append(4)
        lista.append(3)
        print(f"Lista antes de ordenar: {lista}")
        lista.sort()
        print(f"Lista después de ordenar: {lista}")

    def ejercicio02(self):
        print("Calcula suma, máximo y mínimo de [5,3,8,1,9,3]. ")
        lista = [5, 3, 8, 1, 9, 3]
        print(f"Suma: {sum(lista)}")
        print(f"Máximo: {max(lista)}")
        print(f"Mínimo: {min(lista)}")

    def ejercicio03(self):
        print("¿Qué pasa si haces copia=lista y luego copia.append(4)? ¿Por qué?\n")
        lista = [1, 2, 3]
        copia = lista
        copia.append(4)
        print(f"Lista: {lista}")
        print(f"Copia: {copia}")

        print("Ambas variables apuntan a la misma lista en memoria, por lo que al modificar 'copia', también se modifica 'lista'.\n")

        print("Para evitar esto, se puede usar copia = lista.copy() o copia = list(lista) para crear una copia independiente de la lista original.\n")

        copia = lista.copy()
        copia.append(5)
        print(f"Lista después de copiar y modificar copia: {lista}\n")
        print(f"Copia después de copiar y modificar copia: {copia}\n")