#UVA 7 | Ejercicio 4:
#Ejercicio N°3 | UVA N°3
#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Enunciado:

#Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A
#y otros 5 números pertenecientes a la lista B. Crear una lista C,
#donde cada posición es el resultado de la suma del número en la misma posición en la lista A
#con el número en la misma posición en la lista B. Ejemplo: Se crea A = [1, 2, 3, 4, 5] y
#B = [4, 7, 1, 3, 6] → C = [5, 9, 4, 7, 11]

import random

def crea_lista():
    lista = []
    for i in range(5):
        lista.append(random.randint(1,50))
    return lista
   
def suma_lista(lista_a,lista_b):
    c = []
    for i in range(len(lista_a)):
        suma = lista_a[i] + lista_b[i]
        c.append(suma)
    return c

def impresion(lista_a,lista_b,suma):
    print("La lista A es: ",lista_a)
    print("La lista B es: ",lista_b)
    print("La lista C es: ",suma)
    
def main():
    lista_a = crea_lista()
    lista_b = crea_lista()
    suma = suma_lista(lista_a,lista_b)
    impresion(lista_a,lista_b,suma)

main()
