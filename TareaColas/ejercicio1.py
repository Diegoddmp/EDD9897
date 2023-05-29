def esta_ordenada_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
if esta_ordenada_ascendente(mi_lista):
    print("La lista está ordenada de forma ascendente.")
else:
    print("La lista no está ordenada de forma ascendente.")
