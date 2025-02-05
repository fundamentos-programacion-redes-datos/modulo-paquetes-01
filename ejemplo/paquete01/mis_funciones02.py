"""
    Este módulo forma parte de un paquete en Python y puede ser importado en otros scripts.
"""

# Definición de la función para imprimir un reporte con los datos ingresados
def imprimir_reporte(nombre, apellido, correo, notas, promedio):
    """
    Función que recibe los datos y los muestra en formato de reporte.
    """

    # Se construye la cadena formateada con la información del estudiante
    cadena = f"Reporte de Matrícula\n"\
             f"Nombre: {nombre.upper()}\n"\
             f"Apellido: {apellido.upper()}\n"\
             f"Correo: {correo}\n"\
             f"Notas\n"

    for l in notas:
        cadena = f"{cadena}{l}\n"

    cadena = f"{cadena}Promedio: {promedio:.2f}"

    # Se imprime el reporte en pantalla
    print(cadena)



