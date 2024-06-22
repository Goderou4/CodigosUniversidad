'''
Vamos a ir viendo 
las distintas 
operaciones
principalmente
a) Agregar elementos a una lista,concatenar listas
b) Recorrer una lista
c) Eliminar elementos de una lista
d) Limpiar una lista, entre otros
Tematica: Consola de videojuegos
'''
#Crear una lista vacia y otras con elementos
consolas1 = [] #Lista vacia
consolas2 = ["Play 2","Atari","NES","SNES",]
#Agregar elementos a una lista - metodos append(), insert()
#Agregaremos elementos a la primera lista
consolas1.append("Play5") #Con append siempre agregan elementos al final de la lista
consolas1.append("Xbox One")
consolas1.append("Switch")
print()
print("la lista de las PRIMERAS consolas es: {}".format(consolas1))
consolas2.insert(0,"Dreamcast") #Con insert se especifican la posicion de los elementos
consolas2.insert(-2,"Famicon")
consolas2.insert(1000,"Play1")
print()
print("la lista de las SEGUNDAS consolas es: {}".format(consolas2))
consolas = consolas1+consolas2
print()
print("la lista de las consolas es: {}".format(consolas))
#Recorrer una lista
print()
#a) Recorrer por indice la lista de consolas
largo = len(consolas) #Obtener el largo de la lista
for i in range(1,largo):
    print(f"Elemento {i}: {consolas[i]}")
#b) Recorrer por elementos
print()
i = 1
for cons in consolas:
    print(f"Elementos {i}: {cons}")
    i+=1 #Aumentar el contador 
#Vamos a aprender ahora como agregar elementos a una lista por medio de un ciclo
consolas3 = []
print()
#Agregaremos 4 consolas
for i in range(1,5):
    cons = input(f"indique el nombre de la consola {i}\n")
    consolas3.append(cons)
    #Mostraremos la lista
print()
print(f"La lista de las terceras consolas es: {consolas3}")
#Eliminar elementos de una lista del - pop - remove
#ELminar la segunda consola de la lista de consolas
del consolas[1] #Elimina por posicion
#Eliminar la ultima consola
consolas.pop() #Elimina por pocicion
#Eliminar la consola Switch
consolas.remove("Switch") #Elimina por elemento encontrado
print()
print(f"La lista de las terceras consolas actualizada es: {consolas}")