#Integrantes: Matias Berrios, Yossadec Caceres
""""
La función deberá mostrar en pantalla el valor 
original del arriendo, el valor del descuento
 (no el porcentaje) que aplicó y retornar el valor final.
"""


#Cancha	Valor original

#numero 1 del tipo de pago puede ser Efectivo
#numero 2 del tipo de pago puede ser otro medio de pago

print("arcilla = 20000\nsintetica = 30000\npasto = 25000\ncemento = 15000\n")


#Funcion
def calcularValor(tipoCancha,tipoPago):
    #definir tipo de pago
    Efectivo = 1
    print("Usted elijio {}".format(tipoCancha))
    if tipoPago == Efectivo: 
        ValorFinal = arcilla * 0.2
        ValorFinal = pasto * 0.2
        ValorFinal = cemento * 0.2
        ValorFinal = sintetica * 0.2
        return("El valor de la cancha con el descuento aplicado es de {}".format(ValorFinal))
    else:
        ValorFinal = tipoCancha * 0
        return ("El valor de la cancha sin descuento Es de {}".format("0"))
        
#Programa Principal

arcilla = 20000
sintetica = 30000
pasto = 25000
cemento	= 15000

tipoPago = int(input("ingrese el tipo de pago: "))

tipoCancha = input("ingrese la cancha: ")

while tipoCancha:
    if arcilla:
        print("el arriendo seria 20000")
        break
    elif sintetica:
        print("el arriendo seria 30000") 
        break
    elif pasto:
        print("el arriendo seria 25000")
        break
    elif cemento:
        print("el arriendo seria 15000")
        break
    else:
        print("Cancha no encontrada")
    break   

#Llamada de funcion
print(calcularValor(tipoCancha,tipoPago))