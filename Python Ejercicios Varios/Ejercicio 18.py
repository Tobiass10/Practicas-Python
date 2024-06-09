#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°18:
# devuelve los elementos de la diagonal en una lista
import random

def carga_matriz(m,n):
    matriz = []
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valores = random.randint(1,10)
            matriz[i].append(valores)
    return matriz

def impresion(matriz,lista):
    print("Matriz Cargada: ")
    print(" ")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] , end =" ")          
        print("\n")
    print("La lista es: ",lista(matriz))
        
def lista(matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if ( j == i):
                lista.append(matriz[i][j])
    return lista
    
    
    
def main():
    m = n = 3
    matriz_cargada = carga_matriz(m,n)
    imprimir = impresion(matriz_cargada,lista)
    
    

main()

