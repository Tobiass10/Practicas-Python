#**Ejercicio 2:**

#Cargar una lista con 30 valores, generados aleatoriamente y que no se repitan, comprendidos entre 1 y 70

#Ingresar un dato por teclado, el que deberá estar comprendido entre los valores indicados.

#Buscarlo en la lista obtenido utilizando la búsqueda binaria.

#Si el valor no está, informarlo y permitir el ingreso de un nuevo dato a buscar

#Si el valor está, informar si es un número deficiente

#**Número deficiente:** Número que es mayor a la suma de sus divisores,
#sin considerar el propio número. Ej 8>1+2+4
import random

def carga_lista():
    lista = []
    for i in range(30):
        numero = random.randint(1, 70)
        while numero in lista:
            numero = random.randint(1, 70)
        lista.append(numero)
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

def selection_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[i]):
                if (j != i):
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
    return lista

def es_deficiente(num):
    sum_div = 0
    div = 1
    while div < num:
        if num % div == 0:
            sum_div += div
        div += 1
    return sum_div < num
    
        
def main():
    lista = carga_lista()
    copia = lista.copy()
    ordenar = selection_sort(copia)
    print(ordenar)
    valor = int(input("Ingrese el valor a buscar comprendido entre 1 y 70: "))
    while (valor < 1 or valor > 70):
        valor = int(input("Ingrese el valor a buscar comprendido entre 1 y 70: "))
    busqueda = binary_search(ordenar,valor)
    if busqueda == False:
        while valor not in ordenar:
            print("No se encontro el valor en la lista")
            valor = int(input("Ingrese el valor a buscar comprendido entre 1 y 70: "))
            if valor in ordenar:
              print(f"El numero {valor} esta en la lista")  
    else:
        print(f"El numero {valor} esta en la lista")
        if es_deficiente(valor):
            print("El numero es deficiente")
        else:
            print("El numero no es deficiente")
    
main()