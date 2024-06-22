'''
Crear una funcion en Python que reciba el nombre, apellido y el año de nacimiento de 
una persona y luego calcule y muestre sus datos y la edad y muestra ademas su nombre
'''
#Crear la funcion
def Calcula_Edad(nombre,apellido,anioNac): #Cabecera de funcion
    #Cuerpo de la funcion
    anioActual = 2024
    edad = anioActual - anioNac
    print("Su nombre es: {}, su apellido es {}, y su edad es {} años".format(nombre,apellido,edad))
    return edad #Devuelve la edad
#Programa principal
nomb = input("indique el nombre de la persona: ")
apell = input("indique su apellido: ")
aNac = int(input("indique el año de nacimiento: "))
while aNac<1900 or aNac>2024:
    print("Error, año de nacimiento no valido: ")
    aNac = int(input("ingrese un valor valido: "))
#Proceso y salido
#Llamar (o invocar) a la funcion
edad = Calcula_Edad(nomb,apell,aNac)
#TAREA crear una funcion que reciba la edad y determine si la persona es mayor de edad o menor de edad.
#Habra que modificar la funcion anterior retornando la edad (y se hizo)
#Y luego recuperar en el programa principal  (ya se hizo)