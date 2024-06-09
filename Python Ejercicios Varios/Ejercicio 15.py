#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°15:
#Cada vez q pulsa el numero 5 duplica cantidad de elementos a ingresar.

lista = []
cantidad_elementos = 3
indice = 0

while indice < cantidad_elementos:
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

    if numero == 5:
        cantidad_elementos *= 2

    indice += 1

print("La lista final es:", lista)