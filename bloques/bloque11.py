class BloqueOnce:
    def ejercicio01(self):
        print("Crea un dict de persona con nombre, edad y ciudad. Accede con [] y con get().")

        persona = {
            "nombre": "Juan",
            "edad": 30,
            "ciudad": "Madrid"
        }

        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")
        print(f"Nombre: {persona.get('nombre')}, Edad: {persona.get('edad')}, Ciudad: {persona.get('ciudad')}, País: {persona.get('pais', 'No especificado')}")

    def ejercicio02(self):
        persona = {
            "nombre": "Juan",
            "edad": 30,
            "ciudad": "Madrid",
            "hobbies": ["fútbol", "lectura", "viajar"]
        }

        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

    def ejercicio03(self):
        print("¿Qué pasa si haces copia=datos y luego copia['b']=2? ")

        print("Cuando haces copia=datos, estás creando una referencia al mismo diccionario en memoria. Por lo tanto, cualquier cambio en copia afectará a datos.")
        datos = {"a": 1}
        copia = datos
        copia["b"] = 2
        print(f"Datos: {datos}")
        print(f"Copia: {copia}")

        print("Para evitar esto, se puede usar copia = datos.copy() para crear una copia independiente del diccionario original.")
        datos = {"a": 1}
        copia = datos.copy()
        copia["b"] = 2
        print(f"Datos después de copiar y modificar copia: {datos}")
        print(f"Copia después de copiar y modificar copia: {copia}")