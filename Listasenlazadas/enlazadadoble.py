# Clase que representa un nodo de una lista doblemente enlazada
class NodoDoble: 
    def __init__(self, dato):
        # Cada nodo guarda un dato 
        self.dato = dato
        # Enlace al siguiente nodo 
        self.siguiente = None
        # Enlace al nodo anterior 
        self.anterior = None


# Clase que representa la lista doblemente enlazada completa 
class ListaDoble:
    def __init__(self):
        # Al crear la lista, no hay nodos, por eso:
        self.cabeza = None   # Primer nodo de la lista
        self.cola = None     # Último nodo de la lista

    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        # Se crea un nuevo nodo con el dato dado 
        nuevo = NodoDoble(dato)

        # Si la lista está vacía (no tiene cabeza)
        if not self.cabeza:
            # El nuevo nodo será tanto la cabeza como la cola ya que es bidireccional 
            self.cabeza = nuevo
            self.cola = nuevo
            
        else: #No se ejecuta el if y pasa directamente a else cuando la lista ya tiene elementos
            
            # El último nodo que es la cola actual debe apuntar al nuevo nodo
            self.cola.siguiente = nuevo

            # El nuevo nodo debe apuntar hacia atrás, al nodo que antes era la cola
            nuevo.anterior = self.cola

            # Y finalmente, actualizamos la cola para que sea el nuevo nodo
            self.cola = nuevo

    # Método para recorrer la lista desde la cabeza hacia adelante
    def adelante(self):
        # Empezamos desde la cabeza (primer nodo)
        actual = self.cabeza
        
        while actual: # Se ejecutará el while mientras existan nodos por recorrer
            # Mostramos el dato del nodo actual
            print(actual.dato)
            # Avanzamos al siguiente nodo
            actual = actual.siguiente

        # Cuando ya no hay más nodos, imprimimos "None" para indicar el final
        print("None")
        
    # Método para recorrer la lista desde la cola hacia atrás
    def atras(self):
        # Empezamos desde la cola (último nodo)
        actual = self.cola

        # Pasa lo mismo que en el anterior while
        while actual:
            # Mostramos el dato del nodo actual
            print(actual.dato)
            # Retrocedemos al nodo anterior
            actual = actual.anterior

        # Cuando llegamos al principio, imprimimos "None" para indicar el final
        print("None")


# Ejemplo de uso de la lista doblemente enlazada 

# Se crea una lista doblemente enlazada vacía
l1 = ListaDoble()

# Se agregan varios nodos con diferentes datos
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

# Se recorre la lista de principio a fin
print("Recorrido hacia adelante:")
l1.adelante()

# Se recorre la lista de fin a principio
print("Recorrido hacia atrás:")
l1.atras()
