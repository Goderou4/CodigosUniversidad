'''
Crear diferentes tipos de listas
a) Vamos a crear una lista vacia y mostrarla
b) Vamos a crear una lista con valores numericos y mostrarla
c) Vamos a crear una lista solo con cadenas de caracteres y mostrarla
d) Vamos a crear una lista mixta y mostrarla
e) Vamos a acceder a elementos de cada una de las listas y mostrarla
f) Vamos cambiar el valor de algunos elementos de las listas y mostrarla
Tematica: Dragon Ball
'''
dbz1 = [] #crear una lista vacia
print(dbz1) #Mostrar la lista
print(f"La cantidad de elementos de la lista es: {len(dbz1)}")
#len para obtener cantidad de elementos
print()

nivelKi = [190000,20000,8000,30000]
print(f"Los niveles de Ki son: {nivelKi}")
print(f"La cantidad de niveles ki son: {len(nivelKi)}")
print()
saiyajines = ["Goku","Vegetta","Trunks","Gohan"] 
print(f"Los saiyajines son: {saiyajines}")
print(f"La cantidad de saiyajines {len(saiyajines)}")
androides = ["Cell",18,True,"Cell Junior",21,False]
print(f"La lista de andorides es: {androides}")
print(f"La cantidad de elementos es: {len(androides)}")

#Acceder a elemento de la lista
#print(dbz1[0]) No se accede porque esta vacia

#Supongamos que queremos mostrar el segundo ki de la lista de kis
print(f"El segundo ki de la lista de kis es: {nivelKi[1]}")

#Mostraremos uno por uno todos los sayajines
print()
print(f"El primer saiyajin es: {saiyajines[0]}")
print(f"El segundo saiyajin es: {saiyajines[1]}")
print(f"El tercero saiyajin es: {saiyajines[2]}")
print(f"El cuarto saiyajin es: {saiyajines[3]}")

#Mostrar los datos del primer androide
print(f"El nombre del primer andoride es: {androides[0]}")
print(f"El nombre del primer andoride es: {androides[1]}")
print(f"¿El Androide es peligroso?: {androides[2]}")

#Vamos a cambiar el nivel de ki del tercer elemento
nivelKi[2] = 40000
print(f"Los niveles de Ki son: {nivelKi}")

#Vamos a cambiar el nomre del utlimo saiyajin pr un indique
#el usuario
print()
sj = input("indique el nuevo nombre de un saiyajin")
saiyajines[-1] = sj
print(f"Los saiyajines son: {saiyajines}")