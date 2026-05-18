from bloques import BloqueUno, BloqueDos, BloqueTres, BloqueCuatro, BloqueCinco, BloqueSeis, BloqueSiete, BloqueOcho, BloqueNueve, BloqueDiez, BloqueOnce, BloqueDoce, BloqueTrece, BloqueCatorce, BloqueQuince, BloqueDieciseis, BloqueDiecisiete, BloqueDieciocho, BloqueDiecinueve
from io import StringIO
from contextlib import redirect_stdout
import builtins
import sys
from utils import imprimir_menu, imprimir_resultado, limpiar_pantalla


# menus/menu_general.py

class SalidaEjercicio:
    def __init__(self, salida):
        self.salida = salida

    def write(self, texto):
        sys.__stdout__.write(texto)
        self.salida.write(texto)

    def flush(self):
        sys.__stdout__.flush()
        self.salida.flush()


class Menu:
    def __init__(self):
        self.bloque_uno = BloqueUno()
        self.bloque_dos = BloqueDos()
        self.bloque_tres = BloqueTres()
        self.bloque_cuatro = BloqueCuatro()
        self.bloque_cinco = BloqueCinco()
        self.bloque_seis = BloqueSeis()
        self.bloque_siete = BloqueSiete()
        self.bloque_ocho = BloqueOcho()
        self.bloque_nueve = BloqueNueve()
        self.bloque_diez = BloqueDiez()
        self.bloque_once = BloqueOnce()
        self.bloque_doce = BloqueDoce()
        self.bloque_trece = BloqueTrece()
        self.bloque_catorce = BloqueCatorce()
        self.bloque_quince = BloqueQuince()
        self.bloque_dieciseis = BloqueDieciseis()
        self.bloque_diecisiete = BloqueDiecisiete()
        self.bloque_dieciocho = BloqueDieciocho()
        self.bloque_diecinueve = BloqueDiecinueve()

    def mostrar_menu(self, titulo, opciones):
        return imprimir_menu(titulo, opciones)

    def pausar(self):
        input("\nPresione Enter para volver al menú...")
        limpiar_pantalla()

    def ejecutar_ejercicio(self, ejercicio):
        limpiar_pantalla()
        salida = StringIO()
        input_original = builtins.input

        def input_sin_capturar(mensaje=""):
            sys.__stdout__.write(mensaje)
            sys.__stdout__.flush()
            return input_original()

        try:
            builtins.input = input_sin_capturar
            with redirect_stdout(SalidaEjercicio(salida)):
                ejercicio()
        finally:
            builtins.input = input_original

        imprimir_resultado("RESULTADO DEL EJERCICIO", salida.getvalue())
        self.pausar()

    def main_menu(self):

        while True:

            opcion = self.mostrar_menu("MENÚ GENERAL", [
                "1. Bloque 1 - Introducción a POO",
                "2. Bloque 2 - Constructor __init__",
                "3. Bloque 3 - Variables y Tipos de Datos",
                "4. Bloque 4 - Operadores",
                "5. Bloque 5 - Entrada y Salida",
                "6. Bloque 6 - Condicionales",
                "7. Bloque 7 - Bucles",
                "8. Bloque 8 - Funciones",
                "9. Bloque 9 - Listas",
                "10. Bloque 10 - Tuplas",
                "11. Bloque 11 - Diccionarios",
                "12. Bloque 12 - Conjuntos",
                "13. Bloque 13 - Excepciones",
                "14. Bloque 14 - Decoradores",
                "15. Bloque 15 - Unpacking",
                "16. Bloque 16 - Funciones de Orden Superior",
                "17. Bloque 17 - Archivos y JSON",
                "18. Bloque 18 - Mixins",
                "19. Bloque 19 - Producto y Descuento",
                "0. Salir",
            ])

            match opcion:

                case "1":
                    self.menu_bloque_1()

                case "2":
                    self.menu_bloque_2()

                case "3":
                    self.menu_bloque_3()

                case "4":
                    self.menu_bloque_4()

                case "5":
                    self.menu_bloque_5()

                case "6":
                    self.menu_bloque_6()

                case "7":
                    self.menu_bloque_7()

                case "8":
                    self.menu_bloque_8()

                case "9":
                    self.menu_bloque_9()

                case "10":
                    self.menu_bloque_10()

                case "11":
                    self.menu_bloque_11()

                case "12":
                    self.menu_bloque_12()

                case "13":
                    self.menu_bloque_13()

                case "14":
                    self.menu_bloque_14()

                case "15":
                    self.menu_bloque_15()

                case "16":
                    self.menu_bloque_16()

                case "17":
                    self.menu_bloque_17()

                case "18":
                    self.menu_bloque_18()

                case "19":
                    self.menu_bloque_19()

                case "0":
                    limpiar_pantalla()
                    print("\nSaliendo del sistema...")
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_1(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 1", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_uno.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_uno.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_uno.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_2(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 2", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_dos.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_dos.ejercicio02)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_3(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 3", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_tres.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_tres.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_tres.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_4(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 4", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_cuatro.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_cuatro.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_cuatro.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_5(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 5", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_cinco.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_cinco.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_cinco.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_6(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 6", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_seis.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_seis.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_seis.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_7(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 7", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_siete.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_siete.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_siete.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_8(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 8", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_ocho.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_ocho.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_ocho.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_9(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 9", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_nueve.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_nueve.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_nueve.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_10(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 10", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_diez.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_diez.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_diez.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_11(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 11", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_once.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_once.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_once.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_12(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 12", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_doce.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_doce.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_doce.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_13(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 13", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_trece.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_trece.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_trece.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_14(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 14", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_catorce.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_catorce.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_catorce.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_15(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 15", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_quince.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_quince.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_quince.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_16(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 16", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_dieciseis.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_dieciseis.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_dieciseis.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_17(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 17", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_diecisiete.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_diecisiete.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_diecisiete.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_18(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 18", [
                "1. Ejercicio 1",
                "2. Ejercicio 2",
                "3. Ejercicio 3",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_dieciocho.ejercicio01)

                case "2":
                    self.ejecutar_ejercicio(self.bloque_dieciocho.ejercicio02)

                case "3":
                    self.ejecutar_ejercicio(self.bloque_dieciocho.ejercicio03)

                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")

    def menu_bloque_19(self):

        while True:

            opcion = self.mostrar_menu("BLOQUE 19", [
                "1. Ejercicio 1",
                "0. Volver",
            ])

            match opcion:

                case "1":
                    self.ejecutar_ejercicio(self.bloque_diecinueve.ejercicio01)


                case "0":
                    break

                case _:
                    input("\nOpción inválida. Presione Enter para continuar...")
