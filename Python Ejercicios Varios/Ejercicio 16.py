#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°16:
#Primer elemento queda igual y el resto son suma de la sigueinte posicion
# es decir [1,2,3] debe devolver [1,3,5]

def suma(num):
    lista = []
    lista_aux = []
    while num != -1:
        lista.append(num)
        num = int(input("Ingrese un numero: "))
    lista_aux.append(lista[0])
    for i in range(len(lista)-1):
        lista_aux.append(lista[i] + lista[i+1])
    return lista,lista_aux
        
def main():
    num = int(input("Ingrese un numero: "))
    lista,lista_aux = suma(num)
    print(lista)
    print(lista_aux)

main()
