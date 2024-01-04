# Escribir un programa, que contenga una función que reciba un archivo
#llamado datos_origen.txt y un número N y guarde en otro archivo llamado
#datos_destino.txt las primeras N líneas del archivo datos_origen.txt.
# Nota: El usuario ingresará por teclado la cantidad de líneas a copiar.
#En el caso que se produzca un error al abrir el archivo de datos_origen.txt,
#se deberá guardar en un archivo llamado bitacora.txt un registro con la fecha
#y descripción de la excepción.
#Ej.: 2022-11-07 00:46:59.378128;[Errno 2] No such file or directory: 'datos_origen.txt'.
#Se deben utilizar al menos dos funciones y las excepciones que crea conveniente.
from datetime import datetime

class OutForLines(Exception):
    pass

def bitacora(e):
    with open("bitacora.txt","a") as f:
        f.write(str(datetime.now())[:-7] + ";" + str(e) + "\n")

def transferir_registros(f,registros):
    lineas = f.readlines()
    if len(lineas) > registros:
        with open("destino.txt","w") as f:
            for i in range(registros):
                f.write(lineas[i])
    else:
        raise OutForLines("Fuera de Rango")

def main():
    try:
        registros = int(input("Ingrese la cantidad de lineas a copiar: "))
        with open("origen.txt","r") as f:
            transferir_registros(f,registros)
    except OutForLines as e:
        bitacora(e)
    except ValueError as e:
        bitacora(e)
    except FileNotFoundError as e:
        bitacora(e)
    finally:
        print("El programa finalizo correctamente")
        
main()