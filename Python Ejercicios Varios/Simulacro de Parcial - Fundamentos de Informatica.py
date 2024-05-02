#FUNDAMENTOS DE INFORMÁTICA- INTRODUCCIÓN A LA ALGORITMIA
#SIMULACRO DEL 1 PARCIAL

#Hacer un diagrama de flujo en Pseint y un programa que permita :
#Introducir 5 números entre por teclado entre 10 y 40. SE supone que los números se ingresan correctamente.

#Informar:
#El máximo y el mínimo valor cargado.
#La cantidad de números cargados.
#La suma de los números cargados
#El promedio de los mismos.

def calculaNumeros():
    cont = 0
    suma = 0
    minimo = 50
    maximo = 0
    posMax = 0
    posMin = 0
    for i in range(5):
        num = int(input("Ingrese un numero entre 10 y 45: "))
        while (num > 45 or num < 10):
            num = int(input("Ingrese un numero entre los valores indicados: "))
        cont = cont + 1
        suma += num
        if(maximo < num):
            maximo = num
            posMax = cont
        if(minimo > num):
            minimo = num
            posMin = cont
    promedio = suma / cont
    return cont,suma,maximo,minimo,posMax,posMin,promedio

def imprimir(count,sumatoria,maximos,minimos,poMax,poMin,promedio):
    print(f"Cantidad de numeros: {count}")
    print(f"La sumatoria es: {sumatoria}")
    print(f"El promedio es: {round(promedio)}")
    print(f"El numero maximo es: {maximos} y su posicion es: {poMax}")
    print(f"El numero minimo es: {minimos} y su posicion es: {poMin}")
            
def main():
    count,sumatoria,maximos,minimos,poMax,poMin,promedio = calculaNumeros()
    impresion = imprimir(count,sumatoria,maximos,minimos,poMax,poMin,promedio)
    
main()