class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def buscar_valor(arbol, valor):
    if arbol is None:
        return False

    if arbol.valor == valor:
        return True

    if valor < arbol.valor:
        return buscar_valor(arbol.izquierda, valor)
    else:
        return buscar_valor(arbol.derecha, valor)


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

# Imprimimos los datos almacenados en el árbol
print("Datos almacenados en el árbol:")
imprimir_arbol(arbol)
print()

# Llamamos a la función buscar_valor para buscar el valor 3 en el árbol
valor_buscado = 3
encontrado = buscar_valor(arbol, valor_buscado)

# Imprimimos el resultado
if encontrado:
    print("El valor", valor_buscado, "se encuentra en el árbol.")
else:
    print("El valor", valor_buscado, "no se encuentra en el árbol.")
