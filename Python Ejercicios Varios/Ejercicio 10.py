#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°10:
#Enunciado:

#La universidad necesita un sistema para cargar las notas finales
#de los alumnos.

#Los datos para ingresar son:
#Legajo (número positivo),
#mes (solamente se aceptan los números 3, 6 y 12) y
#nota (número entre 1 y 10).
#La carga de datos termina al ingresar -1 como legajo.
#Validar los datos pedidos. Al finalizar, informar:

#Cantidad de alumnos que promocionaron la materia (nota 7 o más). 

#Cantidad de alumnos que aprobaron (nota 4 o más). 

#Porcentaje de alumnos reprobados. 

#Promedio de notas obtenidas en el mes 6.
cont = 0
aprobaron = 0
desaprobaron = 0
promocionaron = 0
contMesSeis = 0

legajo = int(input("Ingrese el numero de legajo: "))
while (legajo != -1):
    while (legajo < 0):
        legajo = int(input("Ingrese un numero de legajo valido (Legajo > 0): "))
    mes = int(input("Ingrese el numero de mes 3,6,12: "))
    while not(( mes == 3) or (mes == 6) or (mes == 12)):
        mes = int(input("Ingrese un numero de mes valido (3,6,12): "))
    nota = int(input("Ingrese la nota: "))
    while (nota > 10 or nota < 1):
        nota = int(input("Ingrese un numero de nota valido: "))
    cont += 1
    if (mes == 6):
        contMesSeis += 1
    if (nota >= 7):
        promocionaron += 1
    if(nota >= 4):
        aprobaron += 1
    if(nota < 4):
        desaprobaron += 1
    legajo = int(input("Ingrese el numero de legajo: "))

print("La cantidad de alumnos que promocionaron: ",promocionaron)
print("La cantidad de alumnnos que aprobaron: ",aprobaron)
print("El porcentaje de alumnos desaprobados es: " + "%",round(desaprobaron * 100 / cont))
print("El promedio de notas obtenidas en el mes 6 es: ", contMesSeis)     
