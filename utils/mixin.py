import re
import json

class ValidationMixin:

    @staticmethod
    def validar_campo(data, nombre_del_campo):
            if not data.strip():
                raise ValueError(f"No ingresar datos vacios para {nombre_del_campo}")


            return data
    
    @staticmethod
    def validar_numero_entero(valor, nombre_del_campo):
        try:
            valor_int = int(valor)
            if valor_int <= 0:
                raise ValueError(f"Por favor, ingrese un número entero positivo para {nombre_del_campo}.")
        except ValueError:
            raise ValueError(f"Por favor, ingrese un número entero válido para {nombre_del_campo}.")

        return valor_int
    
    @staticmethod
    def validar_numero_float(valor, nombre_del_campo):
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ValueError(f"Por favor, ingrese un número entero positivo para {nombre_del_campo}.")
        except ValueError:
            raise ValueError(f"Por favor, ingrese un número entero válido para {nombre_del_campo}.")

        return valor_float

    @staticmethod
    def validar_nota(valor, nombre_del_campo):
        try:
            valor_float = float(valor)
            if valor_float < 0 or valor_float > 10:
                raise ValueError(f"Por favor, ingrese una nota entre 0 y 10 para {nombre_del_campo}.")
        except ValueError:
            raise ValueError(f"Por favor, ingrese una nota válida entre 0 y 10 para {nombre_del_campo}.")

        return valor_float
    
    @staticmethod
    def validar_numero_denominador(valor, nombre_del_campo):
        try:
            valor_int = int(valor)
            if valor_int < 0:
                raise ValueError(f"Por favor, ingrese un número entero positivo para {nombre_del_campo}.")
        except ValueError:
            raise ValueError(f"Por favor, ingrese un número entero válido para {nombre_del_campo}.")

        return valor_int
    
    @staticmethod
    def validar_mayor_edad(edad, nombre_del_campo):
        try:
            valor = int(edad)
            if valor < 18:
                raise ValueError(f"Por favor, ingrese una edad valida para {nombre_del_campo}.")
        except ValueError:
            raise ValueError(f"Ingresar dato valido para {nombre_del_campo}")
        
        return valor
    
    @staticmethod
    def validar_correo(correo, nombre_del_campo):
        patron = r"^[\w\.-]+@((gmail|hotmail|outlook)\.com|unemi\.edu\.ec)$"
        try:
            if not re.match(patron, correo):
                raise ValueError(f"Por favor ingresar el {nombre_del_campo} correctamente")
        except ValueError:
            raise ValueError(f"Por favor, ingrese un dato valido para {nombre_del_campo}")
        
        return correo
    
    @staticmethod
    def pedir_dato_valido(mensaje, funcion_validacion, campo):
        while True:
            try:
                dato = input(mensaje)
                dato = funcion_validacion(dato, campo)
                return dato
            except ValueError as e:
                print(e)

    @staticmethod
    def calcular_promedio(notas):
        promedio = sum(notas) / len(notas)
        return promedio
    
    @staticmethod
    def validar_descuento(valor, nombre_del_campo):

        valor = float(valor)

        if valor < 0 or valor > 100:
            raise ValueError(
            f"El {nombre_del_campo} debe estar entre 0 y 100"
                )

        return valor
    
    @staticmethod
    def validar_str(valor, nombre_del_campo):

        valor = valor.strip()

        if not valor.replace(" ", "").isalpha():
            raise ValueError(
            f"El {nombre_del_campo} solo debe contener letras"
            )

        return valor
    
    
    
    
class ExportarMixin:

    #diccionario a json
    @staticmethod
    def exportar_json(datos):
        return json.dumps(datos, indent= 4, ensure_ascii = False)
    

    # diccionario a csv
    @staticmethod
    def exportar_csv(datos):
        encabezados = datos[0].keys()
        filas= []

        filas.append(",".join(encabezados))

        for dato in datos:
            fila = []
            for encabezado in encabezados:
                fila.append(str(dato[encabezado]))
            
            filas.append(",".join(fila))

        return "\n".join(filas)
