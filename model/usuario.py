class Usuario:
    def __init__(self, nombre, correo, edad):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad

    def info(self):
        return (f"Nombre del usuario: {self.nombre}\nCorreo del usuario: {self.correo}\nEdad del usuario: {self.edad}")