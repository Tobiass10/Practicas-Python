#UVA 6 | Ejercicio 3:
#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Enunciado:

#Diseñar dos funciones llamadas descuento y recargo: ambas recibirán un precio y
#un porcentaje (número entero entre 1 y 30). La primera devolverá el precio con el descuento aplicado,
#mientras que la segunda lo hará con el recargo aplicado.  
#Desarrollar un programa principal que solicite precios hasta ingresar -1.
#Además, deberá solicitar el tipo de operación: 1: Descuento y 2: Recargo. Luego de cada ingreso deberá mostrar
#el precio con descuento o recargo de acuerdo a lo ingresado por el usuario. Validar que puedan ingresar
#solamente esas dos opciones.
#Mostrar la suma total de precios considerando todos los descuentos y recargos aplicados.

def descuento(precio,porcentaje):
    desc = precio - (precio * porcentaje / 100)
    return desc
    
def recargo(precio,porcentaje):
    rec = precio + (precio * porcentaje / 100)
    return rec

def main():
    suma = 0
    precio = float(input("Ingrese valor a pagar: "))
    while (precio != -1):
        while (precio < 0):
            precio = float(input("Ingrese un precio valido: "))
        menu = int(input("Ingrese una opcion: " + "\n" + "1- Descuento" + "\n" + "2- Recargo" + "\n"))
        while not(menu == 1 or menu == 2):
            print("Operacion mal ingresada")
            menu = menu = int(input("Ingrese una opcion valida: 1.Descuento o 2.Recargo "))
        porcentaje = int(input("Ingrese el valor del recargo/descuento entre 1 y 30: "))
        while (porcentaje > 30 or porcentaje < 1):
            porcentaje = int(input("Ingrese un valor de recargo/descuento entre 1 y 30 valido: "))
        if menu == 1:
            des = descuento(precio,porcentaje)
            suma += des
        if menu == 2:
            reca = recargo(precio,porcentaje)
            suma += reca
        precio = float(input("Ingrese valor a pagar: "))
    print("La suma total con los recargos y los descuentos es: ",suma)
    
main()