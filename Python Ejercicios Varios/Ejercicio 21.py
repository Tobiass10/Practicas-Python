#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ingresar un número entero y positivo y generar la siguiente serie

#Si el valor es impar, multiplicarlo por 3 y sumarle 1; si el valor es par, dividirlo por 2.

#Evaluar el resultado obtenido e Ir repitiendo las operaciones, según corresponda, hasta que el valor final sea 1

#Por ejemplo, se ingresa el 7

#7*3+1=**22**/2=**11***3+1=**34**/2=**17***3+1=**52**/2=**26**/2=**13***3+1=**40**/2=**20**/2=**10**/2=**5***3+1=**16**/2=**8**/2=**4**/2=**2**/2=**1**

#Se solicita:

#- Ir guardando los resultados obtenidos en una lista
#- Informar cuantos valores se guardaron en la lista
#- Informar si en la lista hay valores primos, y cuantos. Determinar si el valor es primo con una función
#- Mostrar la lista original con los valores separados por 3 espacios
#- Ordenar la lista de manera descendente y volverla a mostrar

#**Número primo:** Número divisible solamente por 1 y por si mismo. Ej 5

def calculo(num):
    lista = []
    while num > 1:
        if num % 2 != 0:
            num = (num * 3) + 1
        else:
            num = num // 2
        lista.append(num)
    return lista

def recorre_lista(lista):
    cont = 0
    for i in range(len(lista)):
        cont += 1
    return cont


def esPrimo(lista):
    primos=0
    for i in range(len(lista)):
        div,contdiv=1,0
        while div<lista[i]:
            if lista[i]%div==0:
                contdiv=contdiv+1
            div=div+1
        if contdiv<2:
            primos=primos+1
    return primos

def selection_sort(lista):
    for i in range(0, len(lista)-1):
        pos_minimo = i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[pos_minimo]):
                pos_minimo = j
        if (pos_minimo != i):
            aux = lista[pos_minimo]
            lista[pos_minimo] = lista[i]
            lista[i] = aux
    return lista

def separados(lista):
    for i in range(len(lista)):
        print(lista[i] , end = "   ")
    

def main():
    num = int(input("Ingrese un numero entero positivo: "))
    while num <= 1:
        num = int(input("Ingrese un numero entero positivo: "))
    operacion = calculo(num)
    cantidadValores = recorre_lista(operacion)
    primos = esPrimo(operacion)
    ordenamiento = selection_sort(operacion)
    print("La lista ordenada es: ", ordenamiento)
    print("La cantidad de items de la lista es: ", cantidadValores)
    print("La cantidad de numeros primos es: ",primos)
    separados(ordenamiento)
 
main()