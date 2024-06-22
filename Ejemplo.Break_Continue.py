'''
Pedir por teclado una serie de numeros enteros positivos, 
para adivinar el que teniamos pensado al comienzo. 
Cuando el numero ingresado por teclado coincida con el 
numero inicial paramos de solicitar numeros. Cuando la 
persona ingrese un numero negativo o un 0 no lo vamos a considerar
como intento 
'''

#Entrada
numeroinicial = 7
#Solicitar al usuario que adivine el numero
intentos = 0 #Cantidad de intentos de la persona
print("---------Juego Adivina el numero-------------")
print()
while True: #Ciclo infinito
    num = int(input("Adivine el numero: "))
    if num == numeroinicial: #Si el numero coincide con el inicial 
        print("Felicidades Ud. adivino el numero: ")
        intentos+=1
        break #Paramos el juego (ciclo)
    elif num<=0:
        continue #Omite la iteracion
    else:
        print("No, no, no, no, es el numero ;-(, intente nuevamente")
    intentos += 1
#Salida
print("La cantidad de intentos que realizo fue de {}".format(intentos))
print("Juego terminado")