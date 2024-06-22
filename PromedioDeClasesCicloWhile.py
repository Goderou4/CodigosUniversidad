"""
Supongamos que un profe tiene que caclular el promedio final de 
notas de N estudiantes (validar que N>0)de un curso
(pedir el nombre del curso y validar que se escriba)
y para ello debe saber el nombre (validar que se escribas) y la 
nota de cada estudiante y decirle si aprobo o no (considerantdo nota>=4.0 aprueba). 
Validar que cada nota ingresada este entre 1.0 y 7.0
Resolver primero con ciclo while y luego con ciclo for
"""
curso = (input("Indique el nombre del curso: "))
if curso.isalpha():
    pass
else:
    print("ERROR: porfavor ingrese el 'nombre'")
#Uds. se encargan de validar que el curso tenga texto(que tenga nombre)
N = int(input("indique en la cantidad de estudiantes: "))
i = 1 #Contador de estudiantes 
sumaNotas = 0 #Acumulador de notas
#Proceso
while i<=N: #Mientras no recorramos todos los el curso
    print("Estudiante {}".format(N))#Mostrar estudiante en que vamos
    nombreEstud = input("indique su nombre: ")
    #Uds. se encargan de validar que el estudiante tenga nombre
    nota = float(input("indique su nota final: "))
    sumaNotas+=nota#Vamos acumulando la nota
    if nota>=4.0:
        print("Usted aprobo {} el curso de {}".format(nombreEstud,curso))
    else:
        print("Usted repbrobo {} el curso de {}".format(nombreEstud,curso))
    #Pasar al siguiente estudiante
    i +=1
    print()

#Salida
promedio = sumaNotas/N
print ("El promedio del curso {} es {} ".format(curso,promedio))