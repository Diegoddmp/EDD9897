import random

def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Generar lista aleatoria
lista = [random.randint(1, 100) for _ in range(10)]

# Imprimir lista antes de ordenarla
print("Lista original:", lista)

# Ordenar la lista utilizando el algoritmo de selección sort
lista_ordenada = seleccion_sort(lista)

# Imprimir lista después de ordenarla
print("Lista ordenada:", lista_ordenada)
