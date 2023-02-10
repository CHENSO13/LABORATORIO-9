
class Nodo:
    def __init__(self,data):
        self.data = data
        self.siguiente = None


class ListaCircular():
        
    def __init__(self):
        self.inicio = None
    
    def listavacia(self):
        return self.inicio == None
    
    def agregar_inicio(self, data):
        nodo = Nodo(data)
        aux = self.inicio
        nodo.siguiente = self.inicio
        if self.inicio is not None:
            while aux.siguiente != self.inicio:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo
        else:
            nodo.siguiente = nodo
        self.inicio = nodo
            
    def agregar_ultimo(self, data):
        nodo = Nodo(data)
        if self.inicio is None:
            self.inicio = nodo
            nodo.siguiente = self.inicio
        else:
            aux2 = self.inicio
            while aux2.siguiente != self.inicio:
                aux2 = aux2.siguiente
            aux2.siguiente = nodo
            nodo.siguiente = self.inicio

            
    def eliminar_ultimo(self):
        if self.inicio is None:
            return "lista vacia"
        elif self.inicio.siguiente == self.inicio:
            aux = self.inicio
            self.inicio = None
            return str(aux.data)
        else:
            aux = self.inicio
            while aux.siguiente.siguiente != self.inicio:
                aux = aux.siguiente
            aux2 = aux.siguiente
            aux2.siguiente = self.cabeza
            return str(aux2.data)
            
    def eliminar_inicio(self):
        if self.inicio is None:
            return "La lista está vacía"
        elif self.inicio.siguiente == self.inicio:
            aux = self.inicio
            self.inicio = None
            return str(aux.data)
        else:
            aux = self.cabeza
            while aux.siguiente != self.inicio:
                aux = aux.inicio
            aux2 = self.inicio
            self.inicio = self.inicio.siguiente
            aux.siguiente = self.inicio
            return str(aux2.data)

    def mostrar_lista(self):
        if self.inicio is None:
            return "Lista vacia"
        else:
            aux = self.inicio
            lista = []
            while aux.siguiente != self.inicio:
                lista.append(aux.data)
                aux = aux.siguiente
            lista.append(aux.data)
            return lista

try:
    if __name__== "__main__":
        opcion = 0
        lista = ListaCircular()
        
        while opcion != 7:
            print('''LISTA CIRCULAR 
        1. agregar al ultimo
        2. eliminar ultimo
        3. agregar inicio
        4. eliminar inicio
        5. mostrar la lista
        6. lista vacia
        7. salir
        ''')
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                data = input("Ingrese un dato: ")
                lista.agregar_ultimo(data)
            elif opcion == 2:
                print(lista.eliminar_ultimo())
            elif opcion == 3:
                data = input("Ingrese un dato: ")
                lista.agregar_inicio(data)
            elif opcion == 4:
                print(lista.eliminar_inicio())
            elif opcion == 5:
                print(lista.mostrar_lista())
            elif opcion == 6:
                if lista.inicio is None:
                    print("lista vacia")
                else:
                    print(("Lista vacia"))
            elif opcion == 7:
                print("Fin")
            else:
                print("Ingrese una de las opciones por favor")
                 
except Exception as e:
    print(e)           

# - Agregar ultimo
# - Eliminar ultimo.
# - Lista Vacía
# - Agregar Inicio
# - Eliminar Inicio
# - Mostrar Lista
