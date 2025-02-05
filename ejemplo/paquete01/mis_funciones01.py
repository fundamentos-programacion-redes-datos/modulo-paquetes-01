"""
    Este módulo pertenece a un paquete y puede ser importado en otros scripts.
"""

# Definición de la función para obtener los datos personales
def obtener_datos_personales():
    """
    Función que solicita al usuario ingresar su nombre y apellido.
    Se genera automáticamente un correo utilizando la función generar_correo.
    """
    # Ingreso de datos por teclado
    nombre_ingresado = input("Ingresar nombre: ")
    apellido_ingresado = input("Ingresar apellido: ")

    # Se llama a la función generar_correo del mismo módulo
    correo_generado = generar_correo(nombre_ingresado, apellido_ingresado)

    # Se retorna un conjunto de valores para este caso
    # formalmente está retornando un tupla de valores:
    return nombre_ingresado, apellido_ingresado, correo_generado



# Definición de la función que obtiene las notas ingresadas por el usuario
def obtener_notas():
    """
        Función que solicita al usuario ingresar 5 notas y las almacena en una lista.
    """
    lista_nota = []
    for i in range(0, 5):
        nota = input("Ingrese nota :")
        nota = float(nota)
        lista_nota.append(nota)
    
    return lista_nota


# Definición de la función que calcula el promedio de las notas
def obtener_promedio(lista_notas):
    """
    Función que calcula el promedio de una lista de notas proporcionada como argumento.
    """
    suma = 0
    for i in lista_notas:
        suma = suma + i
    promedio = suma / len(lista_notas)

    return promedio

# Definición de la función que genera un correo institucional
def generar_correo(nombre, apellido):
    """
    Función que genera un correo institucional en función del nombre y apellido
    pasados como parámetros.
    Los datos se convierten a minúsculas para mantener un formato estándar.
    """

    # Se convierten los valores de nombre y apellido a minúsculas, con la
    # función lower()
    nombre = nombre.lower()
    apellido = apellido.lower()

    # Se construye la dirección de correo electrónico
    correo = f"{nombre}_{apellido}@utpl.edu.ec"

    # Se retorna el correo generado
    return correo
