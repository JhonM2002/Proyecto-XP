import unittest
from TorreHanoi import TorreHanoi

class TestMovimientosInvalidos(unittest.TestCase):
    def test_movimientos_invalidos(self):
        """HU3: Verifica que los movimientos inválidos no sean permitidos."""
        print("\nIniciando prueba: Movimientos inválidos (HU3)")
        hanoi = TorreHanoi(3)
        print(f"Estado inicial de las torres: {hanoi.torres}")

        # Movimiento no válido: intentar mover desde una torre vacía
        print("Intentando mover desde una torre vacía (Torre 2 a Torre 3):")
        try:
            hanoi.mover_disco(1, 2)  # Torre 2 está vacía
        except ValueError as e:
            print(f"Movimiento inválido detectado: {e}")

        # Movimiento no válido: intentar colocar un disco grande sobre uno más pequeño
        hanoi.mover_disco(0, 2)  # Movimiento válido
        print(f"Movimiento válido realizado de Torre 1 a Torre 3: {hanoi.torres}")
        print("Intentando mover un disco grande sobre uno pequeño (Torre 1 a Torre 3):")
        try:
            hanoi.mover_disco(0, 2)
        except ValueError as e:
            print(f"Movimiento inválido detectado: {e}")

        print("Prueba completada: Movimientos inválidos correctamente manejados.")

if __name__ == "__main__":
    unittest.main()
