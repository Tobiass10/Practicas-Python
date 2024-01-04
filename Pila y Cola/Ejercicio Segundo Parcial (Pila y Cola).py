from cola import *
from pila import *
from datetime import datetime
#Ejercicio 1:
#Crear un archivos usuarios.txt donde cargamos legajo, nombre  y luego la informacion la colocamos en un diccionario
# en el cual debemos buscar su numero de legajo y debe devolvernos el nombre,utilizar las excepciones necesarias.
"""
def cargaDatos():
    try:
        with open("usuarios.txt","a") as f:
            legajo = int(input("Ingrese su numero de legajo: "))
            while (legajo != -1):
                nombre = input("Ingrese su nombre: ")
                registro = str(legajo) + ";" + nombre + "\n"
                f.write(registro)
                legajo = int(input("Ingrese su numero de legajo: "))
    except FileNotFoundError:
        print(e)
    except ValueError:
        print(e)

def cargaDiccionario():
    try:
        with open("usuarios.txt","r") as f:
            lineas = f.readlines()
            diccionario = {}
            for legajos in lineas():
                legajo,nombre = legajos.strip().split(";")
                diccionario[legajo] = nombre
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        return diccionario

def busquedaLegajo(diccionario):
    try:
        legajo = int(input("Ingrese el numero de legajo a buscar: "))
        while legajo != -1:
            if(legajo in diccionario.keys()):
                print(f" El numero de legajo es: {diccionario[legajo]} y su nombre es {legajo}")
            else:
                print(f"No se encontro el legajo")
    except ValueError as e:
        print(e)

def main():
    cargaDatos()
    diccionario = cargaDiccionario()
    busqueda = busquedaLegajo(diccionario)
main()
"""
#Ejercicio 2:
#Crear un archivo personas.txt en el cual almacenamos la informacion id,nombre,edad y copiar en un archivo llamado
# resultado.txt a las personas mayores de 18 años. En caso de arrojar error que se escriban en el archivo bitacora.txt
# y ademas usar las excepciones necesarias.
"""

def main():

main()
"""
#Ejercicio 3:
#Enunciado cargar una colaA con numeros flotantes
#y luego cargar una pilaB. Ejemplo = colaA = [1.0,2.0,3.0] , pilaB = [3.0,2.0,1.0]
"""
def cargaCola():
    colaA = inicializar_cola()
    n = float(input("Ingrese un numero: "))
    while (n != 0.0):
        acolar(colaA,n)
        n = float(input("Ingrese un numero: "))
    return colaA

def cargaPila(cola):
    pilaB = inicializar_pila()
    while(no_es_vacia(cola)):
        tope_cola = tope(cola)
        aux = tope_cola
        desapilar(cola)
        apilar(pilaB,aux)
    return pilaB
        
def main():
    cola = cargaCola()
    pila = cargaPila(copia_cola)
    print(cola)
    print(pila)

main()
"""