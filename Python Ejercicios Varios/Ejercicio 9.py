#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°9:
#Enunciado:

#Crear un programa que pida un número de día (ejemplo: 1) y escriba el nombre del día en letras ("lunes"). Verificar que el día esté entre
#1 y 7, e informar en caso de que no lo sea.

def diasDeLaSemana(n):
    while(n > 7 or n < 1):
        n = int(input("Ingrese el numero que corresponde al dia de la semana: "))
    if n == 1:
        print("Lunes")
    elif(n == 2):
        print("Martes")
    elif(n == 3):
        print("Miercoles")
    elif(n == 4):
        print("Jueves")
    elif(n == 5):
        print("Viernes")
    elif(n == 6):
        print("Sabado")
    else:
        print("Domingo")
    
def main():
    n = int(input("Ingrese el numero que corresponde al dia de la semana: "))
    dias = diasDeLaSemana(n)
    
main()
