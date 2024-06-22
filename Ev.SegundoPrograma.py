#integrantes Matias Berrios, Yossadec Caceres

""""
La función deberá mostrar en pantalla el valor 
original del arriendo, el valor del descuento
 (no el porcentaje) que aplicó y retornar el valor final.
"""


#Cancha	Valor original

#numero 1 del tipo de pago puede ser Efectivo
#numero 2 del tipo de pago puede ser otro medio de pago

print("arcilla = 20000\nsintetica = 30000\npasto = 25000\ncemento = 15000\n")


#Instrucciones para determinar total recaudado
#def calcularRecaudado(cantArc, cantSint, cantPas, cantCem):
    








#Programa Principal

#ciclo for
N = int(input("ingrese una cantidad de arriendos: "))

for N in range(0,N):
    
    cancha = input("Que cancha quiere usted: ")
    
    #definicion de variables
    if cancha=="arcilla":
        cancha = 20000
        print (cancha)
    elif "sintentica":
        cancha = 30000
        print(cancha)
    elif "pasto":
        cancha = 25000
        print (cancha)
    elif "cemento":
        cancha = 15000
        print(cancha)