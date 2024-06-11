#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°2:
#Enunciado:

"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def factorial(n):
    lista = []
    for i in range(n):
        if (n == 0) or (n == 1):
            return 1
        else:
            return n * factorial(n-1)
    


def main():
    n = int(input("Ingrese el numero de factorial a calcular: "))
    fact = factorial(n)
    print(fact)
    
main()
