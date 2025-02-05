"""
    Módulo principal del programa que utiliza un paquete de funciones.
    Se realiza la importación de los módulos dentro del paquete para su uso.
"""

# Importación de módulos (mis_funciones01 y mis_funciones02) desde el paquete01
from paquete01.mis_funciones01 import obtener_datos_personales, obtener_notas,\
    obtener_promedio, generar_correo
from paquete01.mis_funciones02 import imprimir_reporte

# Definición de la función principal con el nombre 'inicio'
def inicio():
    """
    Función principal del programa que permite la obtención de datos y la generación del reporte.
    """

    # Se solicitan los datos personales del usuario
    nombre, apellido, correo = obtener_datos_personales()

    # Se solicitan las notas del usuario
    notas = obtener_notas()

    # Se calcula el promedio de las notas ingresadas
    promedio = obtener_promedio(notas)

    # Se imprime el reporte con toda la información recopilada
    imprimir_reporte(nombre, apellido, correo, notas, promedio)


if __name__ == "__main__":
    inicio()  # Se llama a la función principal 'inicio'

