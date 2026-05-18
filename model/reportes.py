from utils import ExportarMixin
class Reporte(ExportarMixin):
    def __init__(self, datos):
        self.datos = datos
    
    def mostrar_json(self):
        print(self.exportar_json(self.datos))

    def mostrar_csv(self):
        print(self.exportar_csv(self.datos))