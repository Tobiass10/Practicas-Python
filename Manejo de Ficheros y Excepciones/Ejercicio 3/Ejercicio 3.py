# Escribir un programa que lea los datos de un archivo llamado divisas.txt,
# y los guarde en una variable diccionario. Ejemplo del diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.
# Luego, que pregunte al usuario por una divisa
# y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# Nota: Se deben utilizar al menos dos funciones y las excepciones que crea conveniente.


def cargarDivisas():
    with open("divisas.txt", "a") as f:
        divisa = input("Ingrese el nombre de la divisa: ").lower()
        while divisa != "*":
            simbolo = input("Ingrese el simbolo: ")
            f.write(divisa + ";" + simbolo + "\n")
            divisa = input("Ingrese el nombre de la divisa: ").lower()
            
def cargarDiccionario():
    try:
        with open("divisas.txt", "r") as f:
            lineas = f.readlines()
            diccionario = {}
            for divisa in lineas:
                nombre, simbolo = divisa.strip().split(";")
                diccionario[nombre] = simbolo  
    except FileNotFoundError as e:
         print(e)
    else:
        return diccionario
    
def buscarDivisa(diccionario):
    divisa = input("Ingrese la divisa a buscar: ").lower()
    if (divisa in diccionario.keys()):
        print("El simbolo es: ", diccionario[divisa], " de la divisa: ", divisa)
    else:
        print("No se encontro la divisa")
         
def main():
    cargarDivisas()
    diccionario = cargarDiccionario()
    buscarDivisa(diccionario)
main()