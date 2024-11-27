def inicializar_torres(n):
    """Inicializa las torres con los discos en la primera torre."""
    return [list(range(n, 0, -1)), [], []]


def mostrar_torres(torres):
    """Muestra el estado actual de las torres."""
    print("\nEstado de las torres:")
    for i, torre in enumerate(torres):
        print(f"Torre {i + 1}: {torre if torre else 'vacía'}")
    print()


def mover_disco(torres, origen, destino):
    """Mueve un disco de una torre a otra si es válido."""
    if not torres[origen]:
        print("Movimiento inválido: la torre de origen está vacía.")
        return False
    if torres[destino] and torres[destino][-1] < torres[origen][-1]:
        print("Movimiento inválido: no puedes colocar un disco más grande sobre uno más pequeño.")
        return False
    torres[destino].append(torres[origen].pop())
    return True


def verificar_victoria(torres, n):
    """Verifica si el jugador ha ganado."""
    return len(torres[2]) == n


def jugar_torre_hanoi():
    """Juego interactivo de la Torre de Hanoi."""
    print("Bienvenido al juego de la Torre de Hanoi")
    print("El objetivo es mover todos los discos de la torre 1 a la torre 3 siguiendo las reglas:")
    print("- Solo puedes mover un disco a la vez.")
    print("- Un disco más grande no puede colocarse sobre uno más pequeño.")
    
    # Solicitar número de discos
    while True:
        try:
            n = int(input("Ingresa el número de discos (mínimo 1): "))
            if n < 1:
                print("Por favor, ingresa un número válido (mínimo 1).")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Inicializar el juego
    torres = inicializar_torres(n)
    movimientos = 0
    
    # Mostrar estado inicial
    mostrar_torres(torres)
    
    # Ciclo del juego
    while not verificar_victoria(torres, n):
        try:
            # Solicitar movimiento
            origen = int(input("Selecciona la torre de origen (1, 2, 3): ")) - 1
            destino = int(input("Selecciona la torre de destino (1, 2, 3): ")) - 1
            
            # Validar selección
            if origen < 0 or origen > 2 or destino < 0 or destino > 2:
                print("Movimiento inválido: selecciona torres entre 1 y 3.")
                continue
            
            # Intentar mover el disco
            if mover_disco(torres, origen, destino):
                movimientos += 1
                mostrar_torres(torres)
        except ValueError:
            print("Por favor, ingresa números válidos.")
    
    # Mensaje de victoria
    print(f"¡Felicidades! Has resuelto la Torre de Hanoi en {movimientos} movimientos.")


if __name__ == "__main__":
    jugar_torre_hanoi()
