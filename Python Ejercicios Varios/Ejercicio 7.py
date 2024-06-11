#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°7:
#Enunciado:

#Realizar un programa que permita obtener la suma,
#resta, multiplicación y división de dos números x e y ingresados por teclado.
#El programa debe imprimir los números pedidos y el resultado de las cuatro operaciones.

def operaciones_mat(x,y):
    suma = x + y
    resta = x - y
    producto = x * y
    if x == 0 or y == 0:
        division = 0
    else:
        division = x / y
    return suma,resta,producto,division

def main():
    x = float(input("Ingrese el primer numero: "))
    y = float(input("Ingrese el segundo numero: "))
    suma,resta,prod,div = operaciones_mat(x,y)
    print(f"La suma de los dos numeros es {suma}")
    print(f"La resta de los dos numeros es {resta}")
    print(f"La multiplicacion de los dos numeros es {prod}")
    print(f"La division de los dos numeros es {div}")
    
    
main()

"""
No aclara si los numeros a ingresar son enteros o reales
por lo que opte que se puedan ingresar valores reales
para que las divisiones den valores reales.

"""
