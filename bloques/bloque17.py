import json
class BloqueDiecisiete:
    def ejercicio01(self):
        print("Escribe 'Python' en un archivo y léelo.")

        # Escribir
        with open("hola.txt", "w") as file:
            file.write("Python")

        # Leer
        with open("hola.txt", "r") as file:
            contenido = file.read()
            print(f"El contenido dentro de 'hola.txt' es {contenido}")



    def ejercicio02(self):
        print("Guarda {'x':10, 'y':20} en JSON y vuelve a cargarlo.")
        datos = {
            "x": 10,
            "y": 20
        }

        #Con esto guardo
        with open("datos.json", "w") as file:
            json.dump(datos, file, indent=4)

        #Con esto cargo
        with open("datos.json", "r") as file:
            cargado = json.load(file)
            print(f"Diccionario cargado: {cargado}")
            print(f"Valor de x: '{cargado["x"]}'\nValor de y: '{cargado["y"]}'")

        
    def ejercicio03(self):
        print("Guarda una lista de 2 usuarios en JSON, carga y recorre con for.")

        usuarios = [{"nombre": "Luis", "edad": 23}, {"nombre": "Melanie", "edad": 20}]

        #Con esto guardo
        with open("usuarios.json", "w") as file:
            json.dump(usuarios, file, indent=4)

        #Con esto cargo
        with open("usuarios.json", "r") as file:
            cargado = json.load(file)
            
        for usuario in cargado:
            print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
            

