# Definir la función para mostrar mensajes
def mostrar_mensaje(mensaje):
    print(mensaje)

# Crear diccionario
datos_persona = {
    "rut": "14012132-7",
    "nombre": "pedro Alonso",
    "apellido": "morales zenteno",
    "edad": 47
}

# Mostrar el diccionario
mostrar_mensaje("Los datos de la persona son: {}".format(datos_persona))

# Mostrar el rut de la persona
rut = datos_persona.get("rut") #Con get acceder a valor en diccionario sabiendo la clave
mostrar_mensaje("\nEl rut de la persona es {}".format(rut))

# Mostrar el nombre completo
mostrar_mensaje("El Nombre completo de la persona es: {} {}".format(datos_persona.get("nombre"), datos_persona.get("apellido")))

# Eliminar la edad de la persona con pop (campo y clave)
datos_persona.pop("edad")
mostrar_mensaje("\n{}".format(datos_persona))

# Agregar al diccionario la fecha de nacimiento de la persona 
datos_persona.setdefault("fecha_nacimiento", "03-08-1977")
mostrar_mensaje("\n{}".format(datos_persona))

# Pedir un telefono de la persona y agregarlo al diccionario
telef = input("Indique un telefono de la persona: ")
datos_persona.setdefault("telefono", telef)
mostrar_mensaje("\n{}".format(datos_persona))


# Mostrar el diccionario completo (esto marcará error porque el diccionario se ha eliminado exitosamente)
try:
    mostrar_mensaje("\n{}".format(datos_persona))
except NameError:
    mostrar_mensaje("\nEl diccionario 'datos_persona' ha sido eliminado exitosamente.")
