from utils import ValidationMixin, ExportarMixin, pedir_formulario
from model import Estudiante, Usuario, Reporte
import json

class BloqueDieciocho(ValidationMixin, ExportarMixin):
    def ejercicio01(self):
        notas = []
        datos_estudiante = pedir_formulario("DATOS DEL ESTUDIANTE", [
            {"nombre": "nombre", "etiqueta": "Nombre", "validacion": self.validar_campo, "campo": "nombre"},
            {"nombre": "cantidad_notas", "etiqueta": "Cantidad de notas", "validacion": self.validar_numero_entero, "campo": "cantidad de nota"}
        ])

        nombre = datos_estudiante["nombre"]
        cantidad_notas = datos_estudiante["cantidad_notas"]
        campos_notas = []

        for i in range(cantidad_notas):
            campos_notas.append({
                "nombre": f"nota_{i}",
                "etiqueta": f"Nota {i + 1}",
                "validacion": self.validar_nota,
                "campo": f"nota {i + 1}"
            })

        datos_notas = pedir_formulario("NOTAS DEL ESTUDIANTE", campos_notas)
        for i in range(cantidad_notas):
            notas.append(datos_notas[f"nota_{i}"])

        promedio = self.calcular_promedio(notas)

        estudiante = Estudiante(nombre, notas)
        print(estudiante.info())

        print(f"El promedio final de {nombre} es {promedio}")

    def ejercicio02(self):
        datos_usuario = pedir_formulario("DATOS DEL USUARIO", [
            {"nombre": "nombre", "etiqueta": "Nombre", "validacion": self.validar_campo, "campo": "nombre"},
            {"nombre": "correo", "etiqueta": "Correo", "validacion": self.validar_correo, "campo": "correo"},
            {"nombre": "edad", "etiqueta": "Edad", "validacion": self.validar_mayor_edad, "campo": "edad"}
        ])

        nombre = datos_usuario["nombre"]
        correo = datos_usuario["correo"]
        edad = datos_usuario["edad"]
        

        usuario = Usuario(nombre, correo, edad)
        print(usuario.info())

    def ejercicio03(self):
        datos = [
        {"nombre": "Ana", "nota": 9},
        {"nombre": "Luis", "nota": 8},
        {"nombre": "María", "nota": 10}
        ]
        reporte = Reporte(datos)
        print("FORMATO JSON:")
        reporte.mostrar_json()

        print("FORMATO CSV:")
        reporte.mostrar_csv()
