from utils import ValidationMixin, JsonManager



class Persona(ValidationMixin, JsonManager):
            data_file_personas = "data/personas.json"

            def __init__(self, nombre, edad):
                self.__nombre = nombre
                self.__edad = edad
                self.db_personas = JsonManager(self.data_file_personas)
                self.personas = self.db_personas.load()

            @property
            def nombre(self):
                return self.__nombre
            
            @property
            def edad(self):
                return self.__edad
            
            def info(self):
                return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
            
            def to_dict(self):
                return {"nombre": self.nombre, 
                        "edad": self.edad}
            
            @staticmethod
            def from_dict(data):
                return Persona(
                    persona_nombre = data["nombre"],
                    persona_edad = data["edad"]
                )
            
            
            def create(self):
                
                
                while True:
                    
                    try:
                        nombre = input("Ingrese el nombre de la persona: ")
                        nombre = self.validar_campo(nombre, "nombre")
                        break
                    except ValueError:
                        print("Por favor, ingrese un nombre válido.")

                while True:
                    try:
                        edad = input("Ingrese la edad de la persona: ")
                        edad = self.validar_numero_entero(edad, "edad")
                        if edad <= 0:
                            print("Por favor, ingrese una edad válida.")
   
                        break
                    except ValueError:
                        print("Por favor, ingrese una edad válida.")

                