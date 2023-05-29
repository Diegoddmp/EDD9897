class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

# Ejemplo de uso
mi_cola = Cola()
mi_cola.encolar(1)
mi_cola.encolar(2)
mi_cola.encolar(3)

while not mi_cola.esta_vacia():
    elemento = mi_cola.desencolar()
    print(elemento)
