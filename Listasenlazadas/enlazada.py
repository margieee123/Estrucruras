# Clase que representa un nodo en una lista enlazada simple
class Nodo():
    def __init__(self, dato):
        # Cada nodo almacena un valor (dato)
        self.dato = dato
        # Y una referencia al siguiente nodo de la lista
        self.siguiente = None


# Clase que representa toda la lista enlazada
class Lista:
    def __init__(self):
        # Al inicio, la lista está vacía, por eso el primer nodo es None
        self.primero = None
        
    # Se crea un método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)  # Se crea un nuevo nodo con el dato recibido

        # Si la lista está vacía, el nuevo nodo pasa a ser el primero y el puntero pasaría a ser none
        if not self.primero:
            # Este if solo sucede al momento de ingresar el primer nodo
            self.primero = nuevo
        else:
            # Si ya hay elementos, se recorre la lista hasta el último nodo 
            # Al momento de ingresar el segundo dato, el primero se iguala a actual para que así el puntero del segundo nodo sea none
            actual = self.primero
            while actual.siguiente:  # Se ingresa al while a partir del tercer nodo
                actual = actual.siguiente
            # Se enlaza el último nodo con el nuevo nodo 
            actual.siguiente = nuevo
            
        return 1  # Se puede usar como confirmación de que se insertó el dato 
    # A partir del tercer nodo, el actual se va pasando de manera consecutiva al nodo anteriormente agregado
    # Método para eliminar un nodo que contenga un dato específico
    def eliminar(self, dato):
        actual = self.primero   # nodo actual que se está revisando 
        anterior = None         # nodo anterior al actual, que al ser el primer dato no tiene anterior y por eso apunta a none
        
        # Se recorre la lista buscando el nodo que contiene el dato
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        
        # Si no se encontró el dato, no se hace nada
        if not actual:
            return
        
        # Si el nodo a eliminar es el primero
        if not anterior:
            self.primero = actual.siguiente # Ahora el primer nodo será el que venía después del nodo que se acaba de eliminar
        else:
            # Si está en medio o al final, se salta el nodo eliminando su referencia
            anterior.siguiente = actual.siguiente 
            
    
    # Método para imprimir todos los datos de la lista
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)  # Muestra el dato del nodo actual
            actual = actual.siguiente  # Avanza al siguiente nodo


# Ejemplo de uso 
lili = Lista()  # Se crea una lista vacía

# Se agregan tres nodos con diferentes tipos de datos
lili.agregar('k')
lili.agregar(999)
lili.agregar(1000)