class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        
    def info(self):
        return (f"Nombre de estudiante: {self.nombre}\nNotas de estudiante:{self.notas}")