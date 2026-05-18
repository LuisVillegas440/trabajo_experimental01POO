class BloqueDoce:
    def ejercicio01(self):
        print("Crea dos conjuntos y calcula unión, intersección y diferencia.")
        conjunto_a = {1, 2, 3, 4, 5}
        conjunto_b = {4, 5, 6, 7, 8}        
        union = conjunto_a | conjunto_b
        interseccion = conjunto_a & conjunto_b
        diferencia_a_b = conjunto_a - conjunto_b
        diferencia_b_a = conjunto_b - conjunto_a
        print(f"Conjunto A: {conjunto_a}")
        print(f"Conjunto B: {conjunto_b}")
        print(f"Unión: {union}")
        print(f"Intersección: {interseccion}")
        print(f"Diferencia (A - B): {diferencia_a_b}")
        print(f"Diferencia (B - A): {diferencia_b_a}")

    def ejercicio02(self):
        print("Elimina los duplicados de [1,2,2,3,3,3,4] usando set.")

        lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
        sin_duplicados = set(lista_con_duplicados)
        print(f"Lista original: {lista_con_duplicados}")
        print(f"Lista sin duplicados: {sin_duplicados}")



    def ejercicio03(self):
        print("Calcula (A|B) - (A&B). Explica el resultado. ")
        conjunto_a = {1, 2, 3, 4, 5}
        conjunto_b = {4, 5, 6, 7, 8}
        union = conjunto_a | conjunto_b
        interseccion = conjunto_a & conjunto_b
        resultado = union - interseccion
        print(f"Conjunto A: {conjunto_a}")
        print(f"Conjunto B: {conjunto_b}") 
        print(f"Unión: {union}")
        print(f"Intersección: {interseccion}")
        print(f"Resultado (A|B) - (A&B): {resultado}")
        print("El resultado sale asi porque (A|B) contiene todos los elementos de ambos conjuntos, mientras que (A&B) contiene solo los elementos comunes. Al restar la intersección de la unión, obtenemos los elementos que están en A o B pero no en ambos, es decir, los elementos únicos de cada conjunto.")