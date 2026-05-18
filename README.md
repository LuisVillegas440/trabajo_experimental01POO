# Trabajo Experimental 01 - POO en Python

Proyecto académico de consola para practicar fundamentos de Programación Orientada a Objetos y conceptos base de Python. La aplicación organiza los ejercicios por bloques temáticos y expone un menú interactivo para ejecutar cada ejercicio de forma individual.

## Requisitos

- Python 3.10 o superior.
- Terminal compatible con secuencias ANSI para limpiar pantalla, mover cursor y dibujar menús.
- No requiere dependencias externas instaladas con `pip`.

## Ejecución

Desde la raíz del proyecto:

```bash
python3 main.py
```

Si tu sistema usa `python` como alias de Python 3:

```bash
python main.py
```

Al iniciar, se muestra el menú general. Desde ahí se selecciona un bloque y luego el ejercicio correspondiente.

## Estructura Del Proyecto

```text
.
├── main.py              # Punto de entrada de la aplicación
├── view/
│   └── menu.py          # Menú general, submenús y ejecución de ejercicios
├── bloques/
│   ├── bloque01.py      # Introducción a POO
│   ├── bloque02.py      # Constructor __init__
│   ├── ...
│   └── bloque19.py      # Ejercicio adicional de producto y descuento
├── model/
│   ├── estudiante.py    # Modelo Estudiante
│   ├── usuario.py       # Modelo Usuario
│   ├── reportes.py      # Modelo Reporte
│   └── producto.py      # Modelo ProductoDescuento
├── utils/
│   ├── mixin.py         # Mixins de validación y exportación
│   ├── pantalla.py      # Utilidades de pantalla, menús, formularios y resultados
│   └── json_manager.py  # Utilidad para lectura/escritura JSON
└── data/
    └── personas.json    # Archivo de datos usado por utilidades JSON
```

## Arquitectura

El flujo principal empieza en `main.py`, donde se instancia `Menu` desde `view`. La clase `Menu` administra la navegación, instancia los bloques y ejecuta cada método de ejercicio.

Cada archivo en `bloques/` contiene una clase con ejercicios relacionados a un tema de la guía. Los ejercicios usan modelos de `model/` cuando necesitan representar entidades, y funciones/mixins de `utils/` para validación, exportación, persistencia o presentación en consola.

La salida de los ejercicios se captura y luego se muestra dentro de un recuadro usando utilidades de `utils/pantalla.py`. Los ejercicios que requieren entrada del usuario utilizan formularios de consola con posicionamiento por coordenadas.

## Componentes Técnicos

- `ValidationMixin`: centraliza validaciones reutilizables como campos vacíos, números enteros, flotantes, edad, correo, descuentos y notas.
- `ExportarMixin`: convierte estructuras de datos a JSON y CSV.
- `pedir_formulario`: renderiza formularios en consola, valida campo por campo y muestra errores dentro del formulario.
- `imprimir_menu`: dibuja menús y submenús centrados en la terminal.
- `imprimir_resultado`: muestra la salida de los ejercicios dentro de un recuadro.
- `JsonManager`: encapsula carga y guardado de archivos JSON.

## Verificación Básica

Para comprobar que los archivos Python no tienen errores de sintaxis:

```bash
python3 -m py_compile main.py view/menu.py utils/*.py bloques/*.py model/*.py
```

## Notas De Uso

- Ejecutar siempre desde la raíz del proyecto para que las rutas relativas funcionen correctamente.
- Los formularios validan los datos antes de continuar.
- Para volver desde un ejercicio al menú, presionar `Enter` cuando el sistema lo solicite.
