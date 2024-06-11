#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio 6:
#Enunciado:

#Cargar un vector A[10], de manera desordenada.
#Ordenarlo por el metodo de seleccion.
#Ingresar un valor por teclado, buscarlo, e informar con una leyenda en que posicion se lo encontro.
#Si no está ,informarlo.
import random

def carga_lista():
    lista = []
    for i in range(10):
        numero = random.randint(1,50)
        lista.append(numero)
    return lista

def selection_sort(lista):
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[j] < lista[i]):
                if (j != i):
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
    return lista
                    
def binary_search(lista,valor):
    index_low = 0
    index_max = len(lista) - 1
    while index_low <= index_max:
        index_middle = (index_low + index_max) // 2
        if valor == lista[index_middle]:
            return True
        elif valor > lista[index_middle]:
            index_low = index_middle + 1
        else:
            index_max = index_middle - 1
    return False

def main():
    lista = carga_lista()
    copia = lista.copy()
    ordenamiento = selection_sort(copia)
    print(ordenamiento)
    valor = int(input("Ingrese el valor a buscar: "))
    busqueda = binary_search(ordenamiento,valor)
    if busqueda == True:
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")
    
    
    
main()
