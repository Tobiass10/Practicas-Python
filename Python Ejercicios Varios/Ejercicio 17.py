#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°17:
#Devuelve la resta de dos listas y las guarda en una lista "C" y
#luego la ordena.
def diferencia(A,B):
    C = []
    for i in range(len(A)):
            C.append(A[i] - B[i])
    return C

def ordenamiento(resta):
    length = len(resta)
    for i in range(length -1):
        for j in range(length -1):
            if (resta[j+1] < resta[j]):
                aux = resta[j]
                resta[j] = resta[j+1]
                resta[j+1] = aux
    return resta
    

def impresion(A,B,lista_uno,lista_dos):
        print("Listas originales: ")
        print(A)
        print(B)
        print(" ")
        print("La lista diferencia es: ",lista_uno)
        print(" ")
        print("La lista ordenada es: ",lista_dos)

def main():
    A = [5,9,8,8,2]
    B = [1,3,7,2,9]
    
    #Resta recibe la resta de las listas A-B
    resta = diferencia(A,B)
    
    #Hace una copia de la original
    original = resta.copy()
    
    
    #Lista ordenada toma la lista desordenada y la ordena
    lista_ordenada = ordenamiento(resta)
    
    #Imprime las dos listas
    imprimir = impresion(A,B,original,lista_ordenada)
    
main()

