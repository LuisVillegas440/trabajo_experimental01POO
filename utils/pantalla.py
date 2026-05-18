from shutil import get_terminal_size
import sys
from textwrap import wrap


def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="")


def limpiar_pantalla():
    print("\033[2J\033[3J\033[H", end="")


def dibujar_borde(x, y, ancho, alto):
    gotoxy(x, y)
    print("+" + "-" * (ancho - 2) + "+", end="")

    for fila in range(1, alto - 1):
        gotoxy(x, y + fila)
        print("|" + " " * (ancho - 2) + "|", end="")

    gotoxy(x, y + alto - 1)
    print("+" + "-" * (ancho - 2) + "+", end="")


def imprimir_centrado(texto, y, ancho_terminal):
    x = max(1, (ancho_terminal - len(texto)) // 2 + 1)
    gotoxy(x, y)
    print(texto, end="")


def imprimir_menu(titulo, opciones):
    ancho_terminal, alto_terminal = get_terminal_size((100, 30))
    ancho_menu = min(max(56, len(titulo) + 10, *(len(opcion) + 8 for opcion in opciones)), ancho_terminal - 4)
    alto_menu = len(opciones) + 7

    x = max(1, (ancho_terminal - ancho_menu) // 2 + 1)
    y = max(1, (alto_terminal - alto_menu) // 2 + 1)

    limpiar_pantalla()
    dibujar_borde(x, y, ancho_menu, alto_menu)

    imprimir_centrado(titulo, y + 1, ancho_terminal)
    gotoxy(x + 2, y + 2)
    print("-" * (ancho_menu - 4), end="")

    for indice, opcion in enumerate(opciones, start=0):
        gotoxy(x + 4, y + 4 + indice)
        print(opcion[: ancho_menu - 8], end="")

    gotoxy(x + 4, y + alto_menu - 2)
    return input("Seleccione una opción: ")


def imprimir_resultado(titulo, contenido):
    ancho_terminal, alto_terminal = get_terminal_size((100, 30))
    lineas_originales = str(contenido).splitlines() or ["Sin salida para mostrar."]
    ancho_resultado = min(max(70, len(titulo) + 10), ancho_terminal - 4)
    ancho_texto = ancho_resultado - 8
    lineas = []

    for linea in lineas_originales:
        if not linea:
            lineas.append("")
            continue

        partes = wrap(linea, width=ancho_texto, replace_whitespace=False, drop_whitespace=False)
        lineas.extend(partes or [""])

    alto_resultado = min(len(lineas) + 7, alto_terminal - 2)
    lineas_visibles = lineas[: alto_resultado - 7]

    x = max(1, (ancho_terminal - ancho_resultado) // 2 + 1)
    y = max(1, (alto_terminal - alto_resultado) // 2 + 1)

    limpiar_pantalla()
    dibujar_borde(x, y, ancho_resultado, alto_resultado)

    imprimir_centrado(titulo, y + 1, ancho_terminal)
    gotoxy(x + 2, y + 2)
    print("-" * (ancho_resultado - 4), end="")

    for indice, linea in enumerate(lineas_visibles):
        gotoxy(x + 4, y + 4 + indice)
        print(linea[:ancho_texto], end="")

    if len(lineas) > len(lineas_visibles):
        gotoxy(x + 4, y + alto_resultado - 3)
        print("Salida recortada por el tamaño de la terminal.", end="")

    gotoxy(x + 4, y + alto_resultado - 2)


def _escribir_directo(texto):
    sys.__stdout__.write(texto)
    sys.__stdout__.flush()


def _gotoxy_directo(x, y):
    _escribir_directo(f"\033[{y};{x}H")


def _limpiar_linea_directa(x, y, ancho):
    _gotoxy_directo(x, y)
    _escribir_directo(" " * ancho)
    _gotoxy_directo(x, y)


def _dibujar_borde_directo(x, y, ancho, alto):
    _gotoxy_directo(x, y)
    _escribir_directo("+" + "-" * (ancho - 2) + "+")

    for fila in range(1, alto - 1):
        _gotoxy_directo(x, y + fila)
        _escribir_directo("|" + " " * (ancho - 2) + "|")

    _gotoxy_directo(x, y + alto - 1)
    _escribir_directo("+" + "-" * (ancho - 2) + "+")


def pedir_formulario(titulo, campos):
    ancho_terminal, alto_terminal = get_terminal_size((100, 30))
    etiqueta_mas_larga = max(len(campo["etiqueta"]) for campo in campos)
    ancho_formulario = min(max(64, len(titulo) + 10, etiqueta_mas_larga + 42), ancho_terminal - 4)
    alto_formulario = len(campos) + 7

    x = max(1, (ancho_terminal - ancho_formulario) // 2 + 1)
    y = max(1, (alto_terminal - alto_formulario) // 2 + 1)
    x_etiqueta = x + 4
    x_valor = x + etiqueta_mas_larga + 8
    ancho_valor = max(18, ancho_formulario - etiqueta_mas_larga - 14)
    y_mensaje = y + alto_formulario - 2

    _escribir_directo("\033[2J\033[3J\033[H")
    _dibujar_borde_directo(x, y, ancho_formulario, alto_formulario)

    x_titulo = max(1, (ancho_terminal - len(titulo)) // 2 + 1)
    _gotoxy_directo(x_titulo, y + 1)
    _escribir_directo(titulo)
    _gotoxy_directo(x + 2, y + 2)
    _escribir_directo("-" * (ancho_formulario - 4))

    for indice, campo in enumerate(campos):
        fila = y + 4 + indice
        _gotoxy_directo(x_etiqueta, fila)
        _escribir_directo(f"{campo['etiqueta']}:")
        _gotoxy_directo(x_valor, fila)
        _escribir_directo("_" * ancho_valor)

    datos = {}

    for indice, campo in enumerate(campos):
        fila = y + 4 + indice

        while True:
            _limpiar_linea_directa(x_valor, fila, ancho_valor)
            valor = input()

            try:
                datos[campo["nombre"]] = campo["validacion"](valor, campo["campo"])
                _limpiar_linea_directa(x + 4, y_mensaje, ancho_formulario - 8)
                break
            except ValueError as error:
                _limpiar_linea_directa(x + 4, y_mensaje, ancho_formulario - 8)
                _escribir_directo(f"Error: {error}"[: ancho_formulario - 8])

    _limpiar_linea_directa(x + 4, y_mensaje, ancho_formulario - 8)
    return datos
