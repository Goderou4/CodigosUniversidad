'''
hoy vamos a practicar operaciones sobre listas especificamente:
sobre listas especificamente:
a) Crear una lista vacia
b) Vamos a generar al menos 7 elementos pidiendo al usuario valores
c) Vamos a mostrar la lista
d) Vamos a crear una copia de una lista
e) Vamos a buscar un elemento en una lista (crear una funcion para aquello)
f) Vamos a ordenar una listade manera ascendente y descendente 
g) Vamos a limpiar una lista
h) Vamos a contar cantidad de ocurrencias de elementos en una lista
i) Vamos a rebanar una lista
j) Vamos a convertir una lista a tupla
*Ciclo infinito con operaciones para agregar, buscar elemento, mostrar lista o salir 
Tematica: frutas
'''
#Crear una lista vacia 
frutas = []
#Agregar valores a la lista
for i in range(3):
    fru = input(f"indique el nombre de la fruta {i+1}: ").title()
    frutas.append(fru)
#Mostrar la lista
print()
print("La lista de frutas es: ")
for fru in frutas:
    print(fru,end=",")

#Crear una copia de una lista
frutas_copia = frutas.copy()
print()
print(f"La copia de la lista de frutas tiene: {frutas_copia}")
#Crear una funcion para BUSCAR elemento en una lista. Forma 2
def buscarFruta2(val,frutas):
    for fru in frutas:
        if fru == val:
            return True 
        return False #Si no encontro la fruta finalmente

#Crear una funcion para BUSCAR elemento en una lista. Forma 1
def buscaFruta(val,frutas):
    return val in frutas #Si encuentra la fruta retorna True sino False
def principal():
    print()
    val = input("indique la fruta a buscar en la lista: ").title()
    respuesta = buscarFruta2(val,frutas) #Llamamos a la funcion de arriba
    #buscar la fruta en la lista
    if respuesta:
        print(f"La fruta {val} esta en la lista")
    else:
        print(f"La fruta {val} no esta en la lista")
principal() #Llamamos a la funcion principal

#Ordenar una lista 
print()
frutas.sort() #odrena la lista
print(f"La lista de frutas ordenada es: {frutas}")
frutas.reverse() #invierte el orden de la lista
print(f"La lista de frutas invertida es: {frutas}")
#limpiar la vista (vaciar)
frutas_copia.clear()
print()
print(f"La lista de frutas ordenada es: {frutas_copia}")

#Contar la cantidad de ocurrencias en una lista
fru = input("indique una fruta para ver cuantas veces aparece en la lista: ").title()
conteo = frutas.count(fru)
print("la cantidad de veces que aparece la fruta {} en la lista es: {}".format(fru,conteo))

#Rebanar una lista (SLICING)
#Vamos a generar una lista rebanada a las tres primeras frutas 
frutas_reb1 = frutas[0:3] #Va a considerar de la posicion 0 a la 2
print()
print("La lista con las 3 primeras frutas es:{}".format(frutas_reb1))
#Vamos a generar una lista de la cuarta furta en adelante
frutas_reb2 = frutas[3:] #Del 4to elemento en adelante
#Vamos a generar una lista el principio hasta el indice 5
frutas_reb3 = frutas[:5] #Del 1er elemento al que tiene
print()
print("La lista rebanada del 4 elemento en adelante es: {}".format(frutas_reb2))
print()
print("La lista rebanada del primer elemento al quinto: {}".format(frutas_reb3))

#Convertir una lista a tupla
frutas = tuple(frutas)
print
print("La tupla de furtas es: {}".format(frutas)) 
frutas2 = ("platano","sandia","melon")
frutas = frutas + frutas2 #Concatenamos las tuplas
print
print("La tupla de furtas es: {}".format(frutas)) 
#Mostrar el tercer elemento y el octavo en la tupla 
print(f"El tercer elemento es: {frutas[2]}")
print(f"El tercer elemento es: {frutas[7]}")