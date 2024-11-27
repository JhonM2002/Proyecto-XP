class TorreHanoi:
    def __init__(self, n):
        """Inicializa las torres con los discos en la primera torre."""
        self.n = n
        self.torres = [list(range(n, 0, -1)), [], []]

    def mostrar_torres(self):
        """Muestra el estado actual de las torres."""
        print("\nEstado de las torres:")
        for i, torre in enumerate(self.torres):
            print(f"Torre {i + 1}: {torre if torre else 'vacía'}")
        print()

    def mover_disco(self, origen, destino):
        """Mueve un disco de una torre a otra si es válido."""
        if not self.torres[origen]:
            raise ValueError("Movimiento inválido: la torre de origen está vacía.")
        if self.torres[destino] and self.torres[destino][-1] < self.torres[origen][-1]:
            raise ValueError("Movimiento inválido: no puedes colocar un disco más grande sobre uno más pequeño.")
        self.torres[destino].append(self.torres[origen].pop())
