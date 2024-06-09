#Alumno: Fernandez Sarso, Tobias Alejo
#Legajo: 1153411
#Materia: Fundamentos de Informatica
#Turno: Noche

#Ejercicio N°14:
#3 listas Nombre, salario, legajo (Validar Legajo, salario > 0).
#Devolver listas ordenadas por salario
#Buscar si el legajo esta o no en la lista

def carga_listas():
    nombres = []
    salarios = []
    legajos = []
    legajo = int(input("Ingrese su numero de legajo: "))
    while (legajo > 0 and legajo != -1):
        nombre = str(input("Ingrese su nombre: "))
        salario = float(input("Ingrese su salario: "))
        legajos.append(legajo)
        nombres.append(nombre)
        while(salario < 0):
            salario = float(input("Ingrese su salario: "))
        salarios.append(salario)

        
        legajo = int(input("Ingrese su numero de legajo: "))

        
    return legajos,nombres,salarios

def salario_max(salarios):
    maximo = 0
    for i in range(len(salarios)):
        if(maximo < salarios[i]):
            maximo = salarios[i]
            
    return maximo

def salario_min(salarios):
    i = 0
    minimo = salarios[i]
    for i in range(len(salarios)):
        if(minimo > salarios[i]):
            minimo=salarios[i]
    return minimo
        

def busqueda_binaria(legajos,valor):
    index_low = 0
    index_max = len(legajos) - 1
    while(index_low <= index_max):
        index_middle = (index_low + index_max) // 2
        if valor == legajos[index_middle]:
            return True
        elif valor > legajos[index_middle]:
            index_low = index_middle + 1
        else:
            index_max = index_middle - 1
    return False
        
    
def ordenar(s_copy,l_copy,n_copy):
    length = len(s_copy)
    for i in range(length - 1):
        for j in range(length -1):
            if (s_copy[j+1] > s_copy[j]):
                aux = s_copy[j]
                s_copy[j] = s_copy[j+1]
                s_copy[j+1] = aux
                
                aux = l_copy[j]
                l_copy[j] = l_copy[j+1]
                l_copy[j+1] = aux

                aux = n_copy[j]
                n_copy[j] = n_copy[j+1]
                n_copy[j+1] = aux
                
    return s_copy,l_copy,n_copy

def impresion(legajos,nombres,salarios,legajos_ordenados, nombres_ordenados, salarios_ordenados,maximo_salario,minimo_salario):
    print("Listado de Legajos: ", legajos)
    print("Lista de Nombres: ",nombres)
    print("Salarios de c/u: " , salarios)
    print(" ")
    print("Listado de Legajos Ordenados respecto a el valor de los sueldos: ", legajos_ordenados)
    print("Lista de Nombres Ordenados respecto a el valor de los sueldos: ",nombres_ordenados)
    print("Salarios de c/u Ordenados: " , salarios_ordenados)
    print("El salario maximo es de: ", maximo_salario)
    print("El salario minimo es de: ", minimo_salario)
    

    
def main():
    legajos,nombres,salarios = carga_listas()
    s_copy = salarios.copy()
    n_copy = nombres.copy()
    l_copy = legajos.copy()
    salarios_ordenados, legajos_ordenados, nombres_ordenados = ordenar(s_copy,l_copy,n_copy)
    maximo_salario = salario_max(salarios)
    minimo_salario = salario_min(salarios)
    impresion(legajos,nombres,salarios,legajos_ordenados, nombres_ordenados, salarios_ordenados,maximo_salario,minimo_salario)
    valor = int(input("Ingrese el numero de legajo a buscar: "))
    if busqueda_binaria(legajos,valor) == True:
        print("El Legajo Existe")
    else:
        print("El legajo no Existe")
        

main()