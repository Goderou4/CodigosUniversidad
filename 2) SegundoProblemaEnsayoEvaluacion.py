def cash(actividad,total,participantes,entradas,comida):
    total -= entradas*participantes
    total -= comida*participantes
    disponible = total
    return disponible

def vaquita_devolver(disponible,participantes):
    if disponible>0:
        parte = disponible//participantes
        return("Se le devuelve a cada amigo ${}".format(parte))
    elif disponible==0:
        return("Se le devuelve 0 a cada amigo")
    elif disponible<0:
        return("No se devuelve nada porque faltó dinero y el informático puso lo que faltaba xd")

#Programa principal
actividad = input("Indique el nombre de la actividad: ")
ACTIVIDAD = actividad.title()
print("Ustedes estan en un {}".format(ACTIVIDAD))

total = int(input("cuanto dinero han juntado: $"))
while total<=0:
    total = int(input("ingrese una cantidad correcta: "))

participantes = int(input("indique la cantidad de participantes de los amigos: ")) 
while participantes==0:
    participantes = int(input("ingrese una cantidad correcta: "))

entradas = int(input("ingrese el valor pagado de las entradas: "))

comida = int(input("ingrese el valor pagado en comida: "))

#Llamar a la funcion
disponible = cash(actividad,total,participantes,entradas,comida) 

print(vaquita_devolver(disponible,participantes))
