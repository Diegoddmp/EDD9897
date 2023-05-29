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


def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        letra = pila.desapilar()
        palabra_invertida += letra

    return palabra == palabra_invertida


# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
