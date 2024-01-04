#Trabajo Practico N°9
#Ejercicio 1:

from pila import *
"""
def carga_pila():
    pnum = inicializar_pila()
    n = int(input("Ingrese elementos a la pila: "))
    while n != -1:
        apilar(pnum,n)
        n = int(input("Ingrese elementos a la pila: "))
    return pnum

def suma_elementos(pila_cargada):
    acum = 0
    for i in range(len(pila_cargada)):
        acum += pila_cargada[i]
    return acum

def impresion(pila_cargada,suma):
    print(pila_cargada)
    print(suma)

def main():
    pila_cargada = carga_pila()
    suma = suma_elementos(pila_cargada)
    impresion(pila_cargada,suma)

main()
"""
#Ejercicio 2:
"""
def carga_pila():
    pnum = inicializar_pila()
    n = int(input("Ingrese elementos a la pila: "))
    while n != -1:
        apilar(pnum,n)
        n = int(input("Ingrese elementos a la pila: "))
    return pnum

def invertir_pila(pila_cargada):
    newPila = pila_cargada[::-1]
    return newPila
    
def impresion(pila_cargada,invPila):
    print(pila_cargada)
    print(invPila)

def main():
    pila_cargada = carga_pila()
    invPila = invertir_pila(pila_cargada)
    impresion(pila_cargada, invPila)
main()
"""
#Ejercicio 3:
def carga_pila():
    pnum = inicializar_pila()
    n = int(input("Ingrese elementos a la pila: "))
    while n != -1:
        apilar(pnum,n)
        n = int(input("Ingrese elementos a la pila: "))
    return pnum

def ordena_pila(copyPila):
    for i in range(len(copyPila)-1):
        for j in range(len(copyPila)-1):
            if (copyPila[j] > copyPila[j+1]):
                aux = copyPila[j]
                copyPila[j] = copyPila[j+1]
                copyPila[j+1] = aux
    return copyPila
    
def impresion(pila_cargada,pila_ordenada):
    print(pila_cargada)
    print(pila_ordenada)

def main():
    pila_cargada = carga_pila()
    copyPila = pila_cargada.copy()
    pila_ordenada = ordena_pila(copyPila)
    impresion(pila_cargada,pila_ordenada)
main()