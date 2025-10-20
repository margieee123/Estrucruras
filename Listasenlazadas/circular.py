# Clase que representa un nodo en una lista circular simple
class Nodo:
    def __init__(self, dato):
        # Cada nodo guarda un valor o dato
        self.dato = dato
        # Y una referencia al siguiente nodo (inicia vacía)
        self.siguiente = None


# Clase que representa la lista circular simple
class Circular:
    def __init__(self):
        # Al inicio la lista está vacía
        self.primero = None   # Primer nodo de la lista
        self.cont = 0         # Lo que cambia de las listas anteriores es que este tiene un contador de nodos, para controlar el recorrido 
    
    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)  # Se crea un nodo nuevo con el dato recibido

        # Si la lista está vacía solo se ejecutará el if
        if not self.primero:
            self.primero = nuevo
            # Como la lista es circular, el nuevo nodo apunta a sí mismo
            nuevo.siguiente = self.primero
        else:
            # Si ya existen nodos, buscamos el último
            actual = self.primero
            # Recorremos hasta que el siguiente nodo sea nuevamente el primero
            # Lo que significa que llegamos al final del ciclo
            while actual.siguiente != self.primero:
                actual = actual.siguiente
                # Se va incrementando el contador durante el recorrido
                self.cont += 1

            # Enlazamos el último nodo con el nuevo
            actual.siguiente = nuevo
            # El nuevo nodo debe apuntar nuevamente al primero para mantener el ciclo
            nuevo.siguiente = self.primero
            # Aumentamos el contador total de nodos
            self.cont += 1
               
    # Agregamos un método para mostrar todos los nodos de la lista
    def mostrar(self):
        actual = self.primero   # Empezamos desde el primer nodo
        i = 0                   # Contador de iteraciones

        # Mientras existan nodos y no haya un ciclo infinito
        while actual and i < self.cont:
            print(actual.dato)          # Mostramos el dato actual
            actual = actual.siguiente   # Avanzamos al siguiente nodo
            i += 1                      # Aumentamos el contador
            

# Ejemplo de uso 

# Se crea una lista circular vacía
k = Circular()

# Se agregan varios elementos
k.agregar(12)
k.agregar(9)
k.agregar(88)
k.agregar(8800)
k.agregar(9988)

# Se muestra el contenido de la lista
print("Elementos en la lista circular:")
k.mostrar()
