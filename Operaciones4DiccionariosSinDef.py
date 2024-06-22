'''
vamos a crear una ficha de una persona con datos personales,
inicialmente partiremos con el rut, nombres, apellidos y edad
a) Mostrar el diccionario
b) Vamos a acceder al rut, nombre y apellidos usando el metodo get()
c) Vamos a eliminar la edad de la persona con pop
d) Vamos a agregar la fecha de nacimiento en su lugar con el metodo setDefault()
e) Vamos a pedir desde teclado otro dato como lo es la telefono
y lo agregaremos con setDefault()
f) Vamos a mostrar nuevamente el diccionario con tods sus datos
'''

#Crear diccionario
datos_persona = {
    "rut":"14012132-7",
    "nombre":"pedro Alonso",
    "apellido":"morales zenteno",
    "edad":47
}
#Mostrar el diccionario
print("Los datos de la persona son: {}".format(datos_persona))
#Mostrar el rut de la persona
rut = datos_persona.get("rut")#Con get acceder a valor en diccionario sabiendo la clave
print()
print("El rut de la persona es {}".format(rut))
#Mostrar el nombre completo
print("El Nombre completo de la persona es: {}".format(datos_persona.get("nombre" + "apellido")))
#Eliminar la edad de la persona con pop (campo y clave)
datos_persona.pop("edad")
print()
print(datos_persona)
#Agregar al diccionario la fecha de nacimiento de la persona 
datos_persona.setdefault("fecha_nacimiento","03-08-1977")
print()
print(datos_persona)
#Pedir un telefono de la persona y agregarlo al diccionario
telef = input("Indique un telefono de la persona: ")
datos_persona.setdefault("telefono",telef)
#
print(datos_persona)
#Eliminar el diccionario
del datos_persona
#Mostrar el diccionario completo
print(datos_persona) # Marcara error porque el diccionario se ha eliminado exitosamente