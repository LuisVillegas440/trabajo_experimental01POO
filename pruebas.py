# # estudiante = {
# #     "nombre": "Luis",
# #     "notas": [88, 92, 95]
# # }
# # print(estudiante["nombre"])
# class Estudiante:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def info(self):
#         return f"Nombre: {self.nombre}, Nota: {self.nota}"
    
# estudiante01 = Estudiante("Ana", [85, 90, 78])

# print(estudiante01.info())

# datos = {"nombre": "Luis",
#          "nota": [88, 92, 95]
#         }

# estudiante = Estudiante(
#     datos["nombre"],
#     datos["nota"]
# )

# print(estudiante.info())

# animal = {
#     "nombre": "Perro",
#     "edad": 5,
#     "raza": "Labrador"
# }
# print(animal.items())

# clientes = {
#     "Nombre": "Ana",
#     "Edad": 25,
# }

# for value, key in clientes.items():
#     print(f"{value} : {key}")

# print("Python", "Java", "C#", "C++", sep=" → ", end="!\n")

# def calcular_suma_y_promedio(num1, num2):
#             suma = num1 + num2
#             promedio = suma / 2
#             return suma, promedio   
        
# suma, promedio = calcular_suma_y_promedio(10, 20)
# print(f"Suma: {suma}, Promedio: {promedio}")


# i = [i for i in range(5)]
# print(i)

# def calcular_cuadrados(*numeros):
#     cuadrados = [x**2 for x in numeros]
#     return cuadrados

# cuadrados = calcular_cuadrados(1,10,3,5,9)
# print(f"Cuadrados: {cuadrados}")

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(f"Factorial de 5: {factorial(5)}")

# def mi_decorador(funcion):
#     def funcion_decorada(*args, **kwargs):
#         print("Acabo de entrar a la función decorada.")
#         args = (10,10) 
        
#         resultado = funcion(*args, **kwargs)
        

#         print("Acabo de salir de la función decorada.")
#         return resultado
    
#     return funcion_decorada



# @mi_decorador
# def sumar(a, b):
#     print("Mi funcion principal")
#     return a + b

# print(sumar(3, 5))

import os 

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="")

def color(codigo):
    print(f"\033[{codigo}m", end="")

os.system("clear")

gotoxy(100, 10)
color(34)

numeros = (10, 20, 30, 40)
primero, *mitad, ultimo = numeros
print(primero, mitad, ultimo)

def multiplicar(a, b, c):
    
    return a * b * c

lista = [2, 3, 4]
print(multiplicar(*lista))

print("Hola desde gotoxy")
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

nuevo = {**diccionario01 , **diccionario02}
print(nuevo)

numeros = [2, 4, 6]

aumentar = list(map(lambda x: x + 1, numeros))
print(aumentar)

with open("prueba.txt", "w") as file:
    file.write("Hola mundo\n")
    file.write("Segundo hola mundo\n")

with open("prueba.txt", "r") as file:
    contenido = file.read()
    print(contenido)
