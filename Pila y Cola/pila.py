import gc

def inicializar_pila():
    pila =[]
    return pila

def apilar(pila, dato):
    return pila.append(dato)

def desapilar(pila):
    return pila.pop()

def tope(pila):
    return pila[-1]

def no_es_vacia(pila):
    return len(pila) != 0

def eliminar_pila(pila):
    del pila
    gc.collect()
    
def copiar_pila(pila):
    return pila.copy()
    