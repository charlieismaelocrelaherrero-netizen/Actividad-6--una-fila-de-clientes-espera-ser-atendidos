
class Cliente:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ColaClientes:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, numero):
        nuevo = Cliente(numero)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None

        atendido = self.frente
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        print("Cliente atendido:", atendido.numero)
        return atendido.numero

    def peek(self):
        if self.frente is None:
            print("La cola está vacía.")
        else:
            print("Próximo cliente:", self.frente.numero)

    def mostrar(self):
        actual = self.frente

        if actual is None:
            print("La cola está vacía.")
            return

        while actual is not None:
            print(actual.numero, end=" -> ")
            actual = actual.siguiente

        print("None")


cola = ColaClientes()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)

print("Cola de clientes:")
cola.mostrar()

cola.peek()

cola.desencolar()

print("Cola después de atender al primer cliente:")
cola.mostrar()
