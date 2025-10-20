# Clase que representa un nodo doblemente enlazado
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato            # Dato que guarda el nodo
        self.siguiente = None       # Enlace al siguiente nodo
        self.anterior = None        # Enlace al nodo anterior


# Clase que representa una lista doblemente enlazada circular
class ListaDoble:
    def __init__(self):
        self.cabeza = None          # Primer nodo de la lista
        self.cola = None            # Último nodo de la lista
        self.cont = 0               # Contador de nodos (para evitar ciclos infinitos)
    
    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo = NodoDoble(dato)     # Creamos un nuevo nodo con el dato
        if not self.cabeza:         # Si la lista está vacía
            self.cabeza = nuevo     # El nuevo nodo será la cabeza
            self.cola = nuevo       # Y también será la cola
        else:
            self.cola.siguiente = nuevo   # La cola actual apunta al nuevo nodo
            nuevo.anterior = self.cola    # El nuevo nodo apunta hacia atrás a la antigua cola
            self.cola = nuevo             # Actualizamos la cola al nuevo nodo
        
        # Enlaces para hacer la lista circular:
        self.cola.siguiente = self.cabeza   # El último nodo apunta al primero
        self.cabeza.anterior = self.cola    # El primero apunta hacia atrás al último
        
        self.cont += 1   # Aumentamos el contador de nodos
    
    
    # Método para recorrer la lista de adelante hacia atrás
    def adelante(self):
        actual = self.cabeza      # Comenzamos desde la cabeza
        i = 0                     # Contador de iteraciones
        while actual and i < self.cont:   # Recorremos solo la cantidad de nodos existentes
            print(actual.dato)            # Mostramos el dato del nodo actual
            actual = actual.siguiente     # Avanzamos al siguiente nodo
            i += 1                        # Incrementamos el contador
    
    
    # Método para recorrer la lista de atrás hacia adelante
    def atras(self):
        actual = self.cola        # Comenzamos desde la cola
        i = 0                     # Contador de iteraciones
        while actual and i < self.cont:   # Recorremos solo los nodos existentes
            print(actual.dato)            # Mostramos el dato del nodo actual
            actual = actual.anterior      # Retrocedemos al nodo anterior
            i += 1                        # Incrementamos el contador


# PRUEBA DEL FUNCIONAMIENTO

l1 = ListaDoble()      # Creamos una lista doblemente enlazada circular
l1.agregar(456)        # Agregamos varios nodos
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

# Recorremos la lista desde la cabeza hacia la cola
l1.adelante()
print("=" * 50)
# Recorremos la lista desde la cola hacia la cabeza
l1.atras()
