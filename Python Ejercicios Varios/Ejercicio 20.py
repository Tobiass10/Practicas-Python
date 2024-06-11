#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°20:
#Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e informar
#si se encuentran o no en la lista, finalizar las búsquedas con -1 e informar cuantas búsquedas
#fueron exitosas y en cuantas no se encontró el valor buscado.

import random

def carga_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,50))
    return lista

def bubble_sort(lista):
    for i in range(len(lista) -1):
        for j in range(len(lista) -1):
            if (lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def binary_search(valor,lista):
    index_low = 0
    index_max = len(lista) - 1
    while (index_low <= index_max):
        index_middle = (index_low + index_max) // 2
        if (valor == lista[index_middle]):
            return True
        elif (valor > lista[index_middle]):
            index_low = index_middle + 1
        else:
            index_max = index_middle - 1
    return False

def impresion(lista):
    print("Lista: ",lista)
    
    
def main():
    cont_exitos = 0
    cont_fracasos = 0
    n = int(input("Ingrese la cantidad de numeros a ingresar en la lista: "))
    lista_cargada = carga_lista(n)
    ordenar_lista = bubble_sort(lista_cargada)
    impresion(ordenar_lista)
    valor = int(input("Ingrese el numero a buscar: "))
    while (valor != -1):
        if (binary_search(valor,ordenar_lista) == True):
            cont_exitos += 1
            print("El numero se encuentra en la lista")
        else:
            cont_fracasos += 1
            print("El numero no se encuentra en la lista")
        valor = int(input("Ingrese otro numero a buscar: "))
    print("La cantidad de Exitos fue: ",cont_exitos)
    print("La cantidad de Fracasos fue: ",cont_fracasos)
    
main()