#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°3:
#Enunciado:

"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 """

def fibonacci():
    lista = []
    for i in range(50):
        if (i == 0):
            lista.append(0)
        elif(i == 1):
            lista.append(1)
        elif(i == 2):
            lista.append(1)
        else:
            fibonacci = lista[i-1] + lista[i-2] 
            lista.append(fibonacci)
    return lista
          
def main():
    fibo = fibonacci()
    print(fibo)
    
main()
