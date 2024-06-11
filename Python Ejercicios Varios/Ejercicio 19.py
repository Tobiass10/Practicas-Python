#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°19:
# Crear una lista de N números generados al azar entre 0 y 100
# pero sin elementos repetidos.Validar que N sea menor o igual a 100.
import random

def carga_lista(n):
    lista = []
    for i in range(n):
        valor = random.randint(0,100)
        if (valor not in lista):
            lista.append(valor)
    return lista
        
def main():
    n = int(input("Cantidad de numeros a agregar entre 0 y 100: "))
    while (n > 100 or n < 0):
        n = int(input("Ingrese la cantidad correcta: "))
    lista_cargada = carga_lista(n)
    print("La lista es: ",lista_cargada)

main()