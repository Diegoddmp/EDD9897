def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Ingresar los datos de la lista por teclado
lista = []
n = int(input("Ingrese la cantidad de elementos en la lista: "))
for i in range(n):
    elemento = int(input("Ingrese el elemento {}: ".format(i+1)))
    lista.append(elemento)

# Imprimir lista antes de ordenarla
print("Lista original:", lista)

# Ordenar la lista utilizando el algoritmo de selección sort
lista_ordenada = seleccion_sort(lista)

# Imprimir lista después de ordenarla
print("Lista ordenada:", lista_ordenada)
