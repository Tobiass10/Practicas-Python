#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche


#Ejercicio 1:
#Se ingresa por teclado, el numero de vendedor y el importe de cada venta realizado por éste.
#El numero de vendedor puede ser 1,2 o 3. Este dato debera controlarse.
#Es un vector,se debera ir cargando el número de vendedor y en otro el importe de cada
#venta, correspondiendose la posicion de uno con la del otro.
#El fin de la carga se indica con el vendedor 0.
#Por fin de la carga, recorrer los vectores e indicar.

# a) Cuanto vendio cada vendedor(en dinero) y cuantas ventas hizo cada vendedor.
# b) Cual fue el vendedor que mas vendio, en dinero y cual fue el vendedor que mas ventas hizo, en cantidad.
# c) Cuantas ventas superiores a $5000 hubo y cual fue el porcentaje de estas en
# relacion a las ventas totales.
"""
def carga_vendedores():
    importe_ventas = []
    vendedores = []
    numero_vendedor = int(input("Ingrese el numero del vendedor: "))
    while (numero_vendedor != 0):
        while (numero_vendedor < 4 or numero_vendedor > 0):
            numero_vendedor = int(input("Ingrese el numero del vendedor: "))
        venta = float(input("Ingrese el valor de la venta: "))
        vendedores.append(numero_vendedor)
        importe_ventas.append(venta)
        numero_vendedor = int(input("Ingrese el numero del vendedor: "))

    return vendedores,importe_ventas
    



def main():
    vendedor,venta = carga_vendedores()
    print(vendedor,venta)
    
    
    
main()
"""


#Ejercicio 2:
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