from utils import ValidationMixin, pedir_formulario
class BloqueSeis(ValidationMixin):
    
    def ejercicio01(self):
        print("===Programa que determine si un número ingresado es par o impar.===")

        datos = pedir_formulario("NUMERO PAR O IMPAR", [
            {"nombre": "numero", "etiqueta": "Numero", "validacion": self.validar_numero_entero, "campo": "numero"}
        ])
        numero = datos["numero"]

        if numero % 2 == 0:
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")

    def ejercicio02(self):
        print("===Asigna calificación letra (A,B,C,D) según nota numérica.===")
        datos = pedir_formulario("CALIFICACION", [
            {"nombre": "nota", "etiqueta": "Nota numerica", "validacion": self.validar_numero_entero, "campo": "nota"}
        ])
        nota = datos["nota"]
        if 90 <= nota <= 100:
            letra = "A"
        elif 80 <= nota < 90:
            letra = "B"
        elif 70 <= nota < 80:
            letra = "C"
        else:
            letra = "D"
       
        print(f"La calificación letra es: {letra}")

    def ejercicio03(self):
        print("===Sistema de login: usuario=='admin' y password=='123' → 'Bienvenido'; si no → 'Acceso denegado'.===")
        usuario = "admin"
        password = "123"
        while True:
            datos = pedir_formulario("LOGIN", [
                {"nombre": "usuario", "etiqueta": "Usuario", "validacion": self.validar_campo, "campo": "usuario"},
                {"nombre": "password", "etiqueta": "Password", "validacion": self.validar_campo, "campo": "password"}
            ])
            usuario_input = datos["usuario"]
            password_input = datos["password"]

            if usuario_input == usuario and password_input == password:
                print(f"Bienvenido")
                break
            else:
                print("Acceso denegado. Intente nuevamente.")
