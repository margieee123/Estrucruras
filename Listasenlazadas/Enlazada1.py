import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def agregarnodo(self, dato):
        new_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = new_nodo
        else:
            nuevonodo = self.cabeza
            while nuevonodo.siguiente:
                nuevonodo = nuevonodo.siguiente
            nuevonodo.siguiente = new_nodo

    def lista(self):
        resultado = []
        nuevonodo = self.cabeza
        while nuevonodo:
            resultado.append(nuevonodo.dato)
            nuevonodo = nuevonodo.siguiente
        return resultado

    # Métodos para cálculos
    def obtener_mayor(self):
        return max(self.lista())

    def obtener_menor(self):
        return min(self.lista())

    def obtener_promedio(self):
        datos = self.lista()
        return sum(datos) / len(datos)

# Crear lista aleatoria
lista = lista_enlazada()
tamaño = random.randint(5, 10)

for _ in range(tamaño):
    lista.append(random.randint(0, 100))

# Resultados
print("Lista:", lista.lista())
print("Número mayor es ", lista.obtener_mayor())
print("Número menor es ", lista.obtener_menor())
print("Su promedio es ", round(lista.obtener_promedio(), 2))
