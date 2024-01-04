import gc

def inicializar_cola():
    cola =[]
    return cola

def acolar(cola, dato):
    return cola.append(dato)

def desacolar(cola):
    return cola.pop(0)

def primero(cola):
    return cola[0]

def no_es_vacia(cola):
    return len(cola) != 0

def eliminar_cola(cola):
    del cola
    gc.collect()
    
def copiar_cola(cola):
    return cola.copy()
    
