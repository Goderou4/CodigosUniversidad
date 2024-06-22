def vaquita(actividad,total,participantes):
    parte = total//participantes
    print("Ustedes estan en un {}. Y entre todos deben juntar {:.2f}".format(ACTIVIDAD,parte))
    return parte


#Programa principal
actividad = input("Indique el nombre de la actividad: ")
ACTIVIDAD = actividad.upper()

total = int(input("indique la cantidad de dinero que deben juntar: $ "))
while total<=0:
    total = int(input("ingrese una cantidad correcta: "))

participantes = int(input("indique la cantidad de participantes de los amigos: ")) 
while participantes==0:
    participantes = int(input("ingrese una cantidad correcta: "))


#Llamar a la funcion 
vaquita(actividad,total,participantes)