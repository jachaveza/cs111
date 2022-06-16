def busqueda_lineal(L, e):
    for i in range(len(L)):
        if L[i] == e:
            # Se encontro el elemento
            # en la lista
            return True
    # No se encontro el elemento
    # en la lista
    return False

def busqueda_binaria(L, e, i, f):
    if i > f:
        return False

    m = int((i+f)/2)
    
    if L[m] == e:
        return True
    elif L[m] > e:
        return busqueda_binaria(L, e, i, m-1)
    elif L[m] < e:
        return busqueda_binaria(L, e, m+1, f)

L = list(range(10000000))
e = int(input("e: "))

import time

t_inicio = time.time()

resultado = busqueda_lineal(L, e)

t_final  = time.time()

print("resultado={}, tiempo(b.lineal)={:.4f}".format(resultado, t_final-t_inicio))


t_inicio = time.time()

resultado = busqueda_binaria(L, e, 0, len(L)-1)

t_final  = time.time()

print("resultado={}, tiempo(b.binaria)={:.4f}".format(resultado, t_final-t_inicio))
