#En este ejercicio deberás crear un programa llamado personas.py que lea los
#datos de un archivo de texto llamado personas.txt e informe cuales son las
#personas que ganan más de $ 450000. Se deberán guardar todos los datos de
#la/s persona/s que cumplan con dicha condición, en otro archivo llamado
#resultados.txt usando el mismo formato que el archivo personas.txt.
#El archivo personas.txt tendrá el siguiente contenido en texto plano (créalo previamente):
# 1;Carlos;Pérez;200000
# 2;Manuel;Heredia;168000
# 3;Rosa;Campos;890000
# 4;David;García;900000
# Los campos del archivo serán por orden: id, nombre, apellido y sueldo.
# En el caso que se produzca un error al abrir el archivo de personas.txt, se deberá guardar en un archivo llamado bitacora.txt un registro con la fecha y descripción de la excepción.
# Ej.: 2022-11-07 00:46:59.378128;[Errno 2] No such file or directory: 'tema1ej3origen1.txt'
# Nota: se deben utilizar al menos dos funciones y las excepciones que crea conveniente.
# Librería para la fecha: from datetime import datetime - Función: datetime.now()
from datetime import datetime

def bitacora(e):
    with open("bitacora.txt", "a") as f:
        f.write(str(datetime.now())[:-7] + ";" + str(e) + "\n")
 
def cargarPersonas():
    try:
        legajo = int(input("Ingresar el legajo de la persona: "))
        with open("origen.txt", "a") as f:
            while legajo != 0:
                nombre = input("Ingrese el nombre del usuario: ")
                apellido = input("Ingrese el apellido del usuario: ")
                salario = int(input("Ingrese el salario del usuario: "))
                registro = str(legajo) + ";" + nombre + ";" + apellido + ";" + str(salario) + "\n"
                f.write(registro)
                legajo = int(input("Ingresar el legajo de la persona: "))
    except ValueError:
        bitacora(e)
 
def cargarResultado():
    try:
        with open("origen.txt", "r") as f:
            registros = f.readlines()
            if(len(registros)):
                with open ("resultados.txt", "w") as f:
                    for dato in registros:
                        salario = int(dato.strip().split(";")[3])
                        if (salario > 450_000):
                            f.write(dato)
            else:
                print("No hay ningun registro para agregar a resultado")
    except FileNotFoundError as e:
        bitacora(e)
    except ValueError as e:
        bitacora(e)
    except IndexError as e:
        bitacora(e)
    finally:
        print("El programa finalizo correctamente")
 
def main():
    cargarPersonas()
    cargarResultado()
main()