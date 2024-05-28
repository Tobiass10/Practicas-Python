#Nombre: Fernandez Sarso, Tobias
#Legajo:1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Enunciado:

#Calcular el IVA(21%) de una factura .

def iva(factura):
    iva = factura * 0.21
    sin_iva = factura
    total = factura + iva
    return sin_iva,iva,total


def main():
    factura = float(input("Ingrese el valor de la factura: "))
    sin_iva,valor_iva,total = iva(factura)
    print(f"El valor total de la factura sin IVA es: ${sin_iva}")
    print(f"El total de la factura con IVA es: ${total}")
    print(f"El IVA es de: ${valor_iva}")
    
main()