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

# Ejemplo de uso
mi_pila = Pila()
mi_pila.apilar(1)
mi_pila.apilar(2)
mi_pila.apilar(3)

while not mi_pila.esta_vacia():
    elemento = mi_pila.desapilar()
    print(elemento)
