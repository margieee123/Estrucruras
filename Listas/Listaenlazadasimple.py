# Clase que reperenta un nodo e
class Node:
    def __init__(self, value):
        self.value = value  # Valor que almacena el nodo
        self.next = None    # Puntero al siguiente nodo

    def __str__(self):
        # Representación del nodo como texto
        return str(self.value)


# Definición de la clase Lista Enlazada (LinkedList)
class LinkedList:
    def __init__(self):
        self.first = None  # Primer nodo de la lista
        self.size = 0      # Tamaño de la lista (cantidad de nodos)

    # Método para agregar un nuevo nodo al final de la lista
    def append(self, value):
        new_node = Node(value)

        # Si la lista está vacía, el nuevo nodo será el primero
        if self.size == 0:
            self.first = new_node
        else:
            # Recorre la lista hasta llegar al último nodo
            current = self.first
            while current.next is not None:
                current = current.next
            # Agrega el nuevo nodo al final
            current.next = new_node

        # Incrementa el tamaño de la lista
        self.size += 1