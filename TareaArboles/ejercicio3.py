class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def encontrar_minimo(arbol):
    # Encuentra el nodo mínimo en el subárbol izquierdo
    if arbol.izquierda is None:
        return arbol
    else:
        return encontrar_minimo(arbol.izquierda)


def eliminar_valor(arbol, valor):
    if arbol is None:
        return arbol

    # Si el valor es menor que el valor del nodo actual, buscar en el subárbol izquierdo
    if valor < arbol.valor:
        arbol.izquierda = eliminar_valor(arbol.izquierda, valor)
    # Si el valor es mayor que el valor del nodo actual, buscar en el subárbol derecho
    elif valor > arbol.valor:
        arbol.derecha = eliminar_valor(arbol.derecha, valor)
    # Si se encuentra el nodo con el valor a eliminar
    else:
        # Si el nodo no tiene hijos o tiene un solo hijo
        if arbol.izquierda is None:
            return arbol.derecha
        elif arbol.derecha is None:
            return arbol.izquierda
        # Si el nodo tiene dos hijos
        else:
            # Encontrar el nodo mínimo en el subárbol derecho como reemplazo
            minimo = encontrar_minimo(arbol.derecha)
            # Copiar el valor del nodo mínimo al nodo a eliminar
            arbol.valor = minimo.valor
            # Eliminar el nodo mínimo del subárbol derecho
            arbol.derecha = eliminar_valor(arbol.derecha, minimo.valor)

    return arbol


# Función para imprimir el árbol en orden
def imprimir_arbol(arbol):
    if arbol is None:
        return
    imprimir_arbol(arbol.izquierda)
    print(arbol.valor, end=" ")
    imprimir_arbol(arbol.derecha)


# Ejemplo de uso
# Creamos el árbol binario de ejemplo
arbol = Nodo(4)
arbol.izquierda = Nodo(2)
arbol.derecha = Nodo(6)
arbol.izquierda.izquierda = Nodo(1)
arbol.izquierda.derecha = Nodo(3)

# Imprimimos el árbol original
print("Árbol original:")
imprimir_arbol(arbol)
print()

# Eliminamos el valor 2 del árbol
valor_eliminar = 2
arbol = eliminar_valor(arbol, valor_eliminar)

# Imprimimos el árbol resultante
print("Árbol después de eliminar el valor", valor_eliminar, ":")
imprimir_arbol(arbol)
