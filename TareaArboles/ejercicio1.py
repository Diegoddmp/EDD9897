class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def contar_nodos(arbol):
    if arbol is None:
        return 0

    # Sumar el nodo actual más los nodos de los subárboles izquierdo y derecho
    return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)


# Ejemplo de uso
# Creamos el árbol binario de ejemplo
arbol = Nodo(1)
arbol.izquierda = Nodo(2)
arbol.derecha = Nodo(3)
arbol.izquierda.izquierda = Nodo(4)
arbol.izquierda.derecha = Nodo(5)

# Llamamos a la función contar_nodos para obtener la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos(arbol)
print("Cantidad de nodos:", cantidad_nodos)
