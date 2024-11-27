from Sistema.juego import Juego


if __name__ == "__main__":
    while True:
        try:
            # Solicitar al usuario el número de discos
            print("Bienvenido al juego de la Torre de Hanoi")
            print("El objetivo es mover todos los discos de la torre 1 a la torre 3 siguiendo las reglas:")
            print("- Solo puedes mover un disco a la vez.")
            print("- Un disco más grande no puede colocarse sobre uno más pequeño.")
            num_discos = int(input("Ingresa el número de discos para la Torre de Hanoi (mínimo 2): "))
            if num_discos < 2:
                print("El número de discos debe ser al menos 2. Por favor, intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Inicializa el juego con el número de discos ingresado
    juego = Juego(num_discos)
    juego.jugar()

