#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°13:
#Ingresar 10 numeros y cada vez q el usuario ingrese 5 debe ingresa 10 numeros mas.
#Hacer una matriz y devolver una lista de los valores de la diagonal de la matriz y otra
#lista con los valores de la matriz diagonal invertida.

import random

def carga_matriz(m,n):
    matriz = []
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valor = random.randint(1,10)
            matriz[i].append(valor)
    return matriz

def impresion(matriz,lista_uno,lista_dos):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] , end = " ")
        print("\n")
    print("Matriz Diagonal: ",lista_uno)
    print("Matriz Diagonal Invertida: ",lista_dos)

def matriz_diagonal(matriz):
    lista_uno = []
    lista_dos = []
    n = len(matriz)
    for i in range(len(matriz)):
        lista_uno.append(matriz[i][i])
        lista_dos.append(matriz[i][n - 1 - i])
    return lista_uno,lista_dos         
        
    
def main():
    m = n = int(input("Ingrese dimension de la matriz: "))
    matriz_cargada = carga_matriz(m,n)
    lista_uno, lista_dos = matriz_diagonal(matriz_cargada)
    impresion(matriz_cargada,lista_uno,lista_dos)

main()