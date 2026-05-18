import json
class BloqueQuince:
    
    def ejercicio01(self):
        print("Desempaqueta (10, 20, 30, 40) → primera, *mitad, ultima.")

        numeros = (10, 20, 30, 40)
        primero, *mitad, ultimo = numeros

        print(f"Del paquete {numeros} el primer elemento es: {primero}, la mitad es: {mitad}, el ultimo es: {ultimo}")



    def ejercicio02(self):
        print("Usa *lista para pasar [2,3,4] como argumentos a multiplicar(a,b,c).")

        def multiplicar(a, b, c):
            return a * b * c
        
        numeros = [2, 3, 4]
        print(f"El resultado de multiplicar {numeros} es: {multiplicar(*numeros)}")

    def ejercicio03(self):
        print("Combina dos diccionarios usando ** sin sobrescribir el original.")

        diccionario01 = {
            "nombre": "Luis",
            "edad": 23,
            "Pais": "Ecuador"
        }

        diccionario02 = {
            "nombre": "Melanie",
            "edad": 21,
            "pais": "Mexico",
            "hobbies": ["pintar", "cantar", "bailar"]
        }
        print(f"Primer diccionario: {json.dumps(diccionario01, indent=4)}\n")
        print(f"Segundo diccionario: {json.dumps(diccionario02, indent= 4)}\n")

        nuevo = {**diccionario01 , **diccionario02}
        print(json.dumps(nuevo, indent=4))

    
