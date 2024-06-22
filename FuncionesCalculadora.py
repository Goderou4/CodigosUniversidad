'''
Vamos a desarrollar una calculadora con las 4 operaciones basicas,
pero cada operacion estara dentro de una funcion correspodiente. 
Se generara un menu de opciones para que la persona elija que 
operacion llevar a cabo, consideramos nombre de la operacion en 
mayuscula. Si la persona elige salir le mostraremos un mensaje y 
terminara el programa 
'''

print()
#Funcion 1
def obtenerPrimerNum():
    num1 = float(input("indique el primer numero: "))
    return num1
#Funcion 2
def obtenerSegundoNum():
    num2 = float(input("indique el segundo numero: "))
    return num2 
#Funcion 2
def obtenerSegundoNum():
    num2 = float("indique el segundo numero: ")
    return num2 
#Funcion 3 - Operacion 1: SUma
def obtenerSuma(num1,num2):
    suma = num1+num2
    return suma
#Uds. haran el resto de las operaciones con funciones 

def salir(): #Procedimiento 
    print("Gracias por usar la calculadora...")

#Procedimiento para crear un menu de opciones
def menu():
    print("------Calculadora simple------")
    print()
    print("SUMA: SUMA DE LOS NUMEROS")
    print("RESTA: RESTA DE LOS NUMEROS")
    print("MULTIPLICACION: MULTIPLICACION DE LOS NUMEROS")
    print("DIVISION: DIVISON DE LOS NUMEROS")
    print("SALIR: SALIR DEL PROGRAMA")
    print()
    print("Elija su opcion")

#Programa principal
while True:
    menu()
    opc = input("indique su opcion: ").upper() #Convierte texto a MAYUSCULA
    if opc == "SUMA":
        n1 = obtenerPrimerNum()
        n2 = obtenerSegundoNum()
        print(f"La suma de {n1} + {n2} es: {obtenerSuma(n1,n2)}")
    elif opc == "SALIR":
        salir()
        break
    else:
        print("Opcion incorrecta")
        print("Programa finalizado")

n1 = obtenerPrimerNum() #Llamamos a la funcion
n2 = obtenerSegundoNum() #Llamamos a la funcion 
