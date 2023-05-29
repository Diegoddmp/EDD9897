class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


def es_simetrica(lista):
    pila = Pila()
    mitad = len(lista) // 2

    for i in range(mitad):
        pila.apilar(lista[i])

    if len(lista) % 2 == 1:
        inicio = mitad + 1
    else:
        inicio = mitad

    for i in range(inicio, len(lista)):
        elemento_pila = pila.desapilar()
        if elemento_pila != lista[i]:
            return False

    return True


# Ejemplo de uso
mi_lista = [1, 2, 3, 2, 1]
if es_simetrica(mi_lista):
    print("La lista es simétrica.")
else:
    print("La lista no es simétrica.")
