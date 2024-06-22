'''
A continuacion presentaremos varios ejemplos de manejo de excepciones
'''
#Vamos pedir dos numeros y realizaremos la division de ambos
while True:
    try: #Bloque donde esta la falla
        num1 = int(input("indique el primer numero: "))
        num2 = int(input("indique el segundo numero: "))
        divi = num1/num2
    except ZeroDivisionError: #Manejo de rrores
        print("Error, no se puede dividir por cero...")
    except ValueError:
        print("Error, tipo de dato no permitido")
    except:
        print("Otro tipo de error...")
    else: #Si todo esta sin errores nuestro resultado o resto de operacion
        print("El resultado de la division es: {:.0}".format(divi))
        break
    finally:
        print("Programa terminado...")

#Vamos a crear una lista con 3 valores y un diccionario con dos elementos

    try:
        lista_edades = [12,18,33]
        dicc_persona = {"rut":"12345","nombre_completo":"Pedro Antonio Lopez Soto"}
        print("La lista de edades es: {}".format(lista_edades))
        print("El diccionario es: {}".format(dicc_persona))
        elem = lista_edades[7] #Situcacion que llevara a falla
        elem2 = dicc_persona["edad"] #Situcacion que va a llevar a falla
        elem3 = lista_edades[0] + "hola" ##Situcacion que llevara a falla
    except IndexError:
        print("Error, indice 7 no existe en la lista")
    except KeyError:
        print("Error no existe la clave edad")
    except TypeError:
        print("Error, tipos de datos no compatible para operaciones")
    else:
        print("El elemento de la lista a mostrar es: {}".format(elem))
        print("El valor en el diccionario a mostrar es: {}".format(elem2))
        print("El resultado de la opreacion es: {}".format(elem3))
    finally:
        print("Programa terminado...")