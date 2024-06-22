'''
Ejemplo de diccionario en Python:
a) Vamos a crear un diccionario
b) Vamos a mostrar el diccionario
c) Vamos a recorrer el diccionario de dos manereas diferentes
d) Vamos a agregar un elemnto al diccionario y mostrar nuevamente 
Tematica: Paises (clave) y Captilaes (valor) del mundo
Tarea: Crear un diccionario de Arboles (clave) y Frutos (valor) 
'''

#Crear diccionario en Python (no vacio)
dicc1 = {"Chile":"Santiago",
         "Peru":"Lima",
         "Argentina":"Buenos Aires",
         "Holanda":"Amsterdam",
         "Haiti":"Puerto Principe",
         "Venezuela":"Caracas"
         }


#Mostrar el diccionario
print()
print(f"El diccionario de paises y captilaes es: {dicc1}")
# Forma 1: Recorrer el diccionario por clave
print("----Forma 1 de recrorrer el diccionario----")
for clave in dicc1.keys(): #Recorre accediendo a la clave
    print(f"{clave}==>{dicc1[clave]}")
# Forma 1: Recorrer el diccionario por clave
print()
print("----Forma 2 de recrorrer el diccionario----")
print()
for valor in dicc1.values(): #Recorre accediendo por valor cada elemento
    print(f"Capital: {valor}") 
# Agregar elemento Paraguay con captial Asuncion
dicc1["Paraguay"] = "Asuncion"
print()
print(f"El diccionario de paises y captilaes es: {dicc1}")


dicc2 = {"Manzano":"manzana",
         "Ciruelo":"Ciruela",
         "Durazno":"Durazno",
         "Naranjos":"Naranja",
         }


# Mostrar el diccionario usando un bucle while
claves = list(dicc2.keys())
i = 0
while i < len(claves):
    clave = claves[i]
    print("{} = {}".format(clave, dicc2[clave]))
    i += 1