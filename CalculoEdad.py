# Definir la función que calcula la edad y determina si es mayor o menor de edad
"""
Esta función recibe el nombre, apellido y año de nacimiento de una persona,
calcula su edad y determina si es mayor o menor de edad.
"""

def calcular_y_determinar_edad(nombre, apellido, anio_nacimiento):
    # Año actual
    anio_actual = 2024
    # Calcular la edad
    edad = anio_actual - anio_nacimiento
    # Imprimir los datos de la persona
    print(f"Su nombre es: {nombre} {apellido}, y su edad es {edad} años.")
    
    # Determinar si es mayor o menor de edad
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")
    
    # Devolver la edad calculada
    return edad

# Programa principal
if __name__ == "__main__":
    # Solicitar al usuario que ingrese su nombre
    nombre = input("Indique el nombre de la persona: ")
    
    # Solicitar al usuario que ingrese su apellido
    apellido = input("Indique su apellido: ")
    
    # Solicitar al usuario que ingrese su año de nacimiento
    anio_nacimiento = int(input("Indique el año de nacimiento: "))
    
    # Validar que el año de nacimiento esté en un rango razonable
    while anio_nacimiento < 1900 or anio_nacimiento > 2024:
        print("Error, año de nacimiento no válido.")
        anio_nacimiento = int(input("Ingrese un año de nacimiento válido: "))
    
    # Llamar a la función y pasar los datos ingresados
    edad = calcular_y_determinar_edad(nombre, apellido, anio_nacimiento)
