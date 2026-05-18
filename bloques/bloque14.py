class BloqueCatorce:
    def ejercicio01(self):
        print("Crea un decorador que imprima 'Iniciando ..' antes de ejecutar la función.\n")

        def mi_decorador(funcion):
            def funcion_decorada(*args, **kwargs):
                print("Iniciando ..")
                resultado = funcion(*args, **kwargs)
                return resultado
            return funcion_decorada
        
        @mi_decorador
        def funcion_principal():
            print("Ejecutando la función principal.\n")

        funcion_principal()


    def ejercicio02(self):
        print("Crea un decorador que verifique que el argumento sea positivo antes de calcular su cuadrado.\n")   
        def decorador_verificar_positivo(funcion):
            def funcion_decorada(numero):
                if numero < 0:
                    print("Error: El número debe ser positivo.")
                    return None
                return funcion(numero)
            return funcion_decorada
        
        @decorador_verificar_positivo
        def calcular_cuadrado(numero):
            return numero ** 2
        
        numero = 5  
        resultado = calcular_cuadrado(numero)
        if resultado is not None:
            print(f"El cuadrado de {numero} es: {resultado}\n")

    def ejercicio03(self):
        print("Analiza @log de suma(a,b). ¿Qué imprime suma(2,3)?\n")

        def log(funcion):
            def funcion_decorada(*args, **kwargs):
                print(f"Llamando a la función: {funcion.__name__}")
                resultado = funcion(*args, **kwargs)
                print(f"Resultado obtenido: {resultado}")
                return resultado

            return funcion_decorada

        @log
        def suma(a, b):
            return a + b

        print(suma(2, 3)) 