#FUNDAMENTOS DE INFORMÁTICA- INTRODUCCIÓN A LA ALGORITMIA
#SIMULACRO DEL 2° PARCIAL

#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Enunciado:
#Generar una lista aleatoria de 5 sueldos entre $   700000 y $1000000. 
#Generar una segunda lista de ½ aguinaldos a partir de la primera lista. 
#½ aguinaldo = sueldo * 0.5

#Imprimir ambas listas y sus longitudes.

#Hacer una tercera lista con la suma del sueldo + el ½ aguinaldo para cada empleado.

#Mediante una función encontrar la suma de cada lista y devolver el resultado al programa ppal. e imprimirlos.

#En el programa ppal. Calcular la suma total de ambas listas e imprimirlas.

#Calcular el promedio de la lista de sueldos y aguinaldos  imprimirlos.

#Encontrar el máximo y el mínimo de la tercera lista y sus posiciones.

#Ordenar la lista de sueldos de  menor a mayor por el método de burbujeo

#Introducir un sueldo por teclado validado y por búsqueda binaria informar si se encuentra o no en la lista

import random

def sueldos():
    lista_sueldos = []
    lista_aguinaldos = []
    lista_sueldo_total = []
    lista_empleados = []
    for i in range(5):
        empleado = i + 1
        sueldo = random.randint(70000,1000000)
        lista_empleados.append(empleado)
        lista_sueldos.append(sueldo)
    for i in range(len(lista_sueldos)):
        aguinaldo = (lista_sueldos[i] * 0.5)
        lista_aguinaldos.append(aguinaldo)
    for i in range(len(lista_aguinaldos)):
        total = lista_sueldos[i] + lista_aguinaldos[i]
        lista_sueldo_total.append(total)
    return lista_empleados,lista_sueldos,lista_aguinaldos,lista_sueldo_total

def suma_total(sueldo,aguinaldo,total):
    suma_total_sueldos = 0
    suma_total_aguinaldos = 0
    suma_total = 0
    for i in range(len(sueldo)):
        suma_total_sueldos += sueldo[i]
    for i in range(len(aguinaldo)):
        suma_total_aguinaldos += aguinaldo[i]
    for i in range(len(total)):
        suma_total += total[i]
    return suma_total_sueldos,suma_total_aguinaldos,suma_total

def ordenamiento(sueldo,aguinaldo):
    for i in range(len(sueldo)-1):
        for j in range(len(sueldo)-1):
            if sueldo[j] > sueldo[j+1]:
                aux = sueldo[j]
                sueldo[j] = sueldo[j+1]
                sueldo[j+1] = aux
                
                aux = aguinaldo[j]
                aguinaldo[j] = aguinaldo[j+1]
                aguinaldo[j+1] = aux
    return sueldo,aguinaldo

def binary_search(valor,lista):
    index_low = 0
    index_max = len(lista) - 1
    while index_low <= index_max:
        index_middle = index_low + index_max // 2
        if valor == lista[index_middle]:
            return True
        elif valor > lista[index_middle]:
            index_low = index_middle + 1
        else:
            index_max = index_middle - 1
    return False
            
def maximo_minimo(lista):
    maximo = 0
    minimo = 0
    posMax = 0
    posMin = 0
    for i in range(len(lista)):
        if (not i):
            maximo = lista[i]
            minimo = lista[i]
        elif (maximo < lista[i]):
            maximo = lista[i]
            posMax = i + 1
        elif (minimo > lista[i]):
            minimo = lista[i]
            posMin = i + 1
    return maximo,minimo,posMax,posMin
    
def impresion(empleados,sueldo,aguinaldo,total,sumatoria_sueldos,sumatoria_aguinaldos,sumatoria_total,sueldos_ord,aguinaldos_ord,maxim,minim,posMaxim,posMinim):
    print(f"Cada posicion de la lista le corresponde a cada N° de Empleado")
    print(f"Empleados Enumerados: {empleados}")
    print(f"Los Sueldos de cada empleados (Ordenados de Menor a Mayor): {sueldo} y la longitud de la lista es: {len(sueldo)}")
    print(f"Los Aguinaldos de cada empleado (Ordenados de Menor a Mayor): {aguinaldo} y la longitud de la lista es: {len(sueldo)}")
    print(f"El Total(Sueldos + Aguinaldos) de cada empleado : {total} y la longitud de la lista es: {len(sueldo)}")
    print("")
    print(f"La sumatoria de sueldos es: {sumatoria_sueldos}")
    print(f"La sumatoria de aguinaldos es: {sumatoria_aguinaldos}")
    print(f"La sumatoria total de todos los sueldos más todos los aguinaldos es: {sumatoria_total}")
    print("")
    print(f"El Sueldo + Aguinaldo mas alto es: {maxim} en la posicion {posMaxim}")
    print(f"El Sueldo + Aguinaldo mas bajo es: {minim} en la posicion {posMinim}")
    print("")
 
def main():
    empleados,sueldo,aguinaldo,total = sueldos()
    sumatoria_sueldos,sumatoria_aguinaldos,sumatoria_total = suma_total(sueldo,aguinaldo,total)
    maxim,minim,posMaxim,posMinim = maximo_minimo(total)
    sueldos_ord,aguinaldos_ord = ordenamiento(sueldo,aguinaldo)
    impresion(empleados,sueldo,aguinaldo,total,sumatoria_sueldos,sumatoria_aguinaldos,sumatoria_total,sueldos_ord,aguinaldos_ord,maxim,minim,posMaxim,posMinim)
    valor = int(input("Ingrese el sueldo a buscar en la lista de sueldos: "))
    if binary_search(valor,sueldo) == True:
        print("El Sueldo esta en la lista")
    else:
        print("El sueldo no esta en la lista")
main()
