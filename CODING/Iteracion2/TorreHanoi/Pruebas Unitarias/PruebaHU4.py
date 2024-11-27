import unittest
from TorreHanoi import TorreHanoi

class TestContarMovimientos(unittest.TestCase):
    def test_contar_movimientos(self):
        """Verifica que el juego cuente correctamente los movimientos válidos realizados y no incluya movimientos no válidos."""
        print("\nIniciando prueba: Contar movimientos válidos y excluir no válidos")
        hanoi = TorreHanoi(3)
        print(f"Estado inicial: {hanoi.torres}")
        
        # Movimiento 1: Válido
        hanoi.mover_disco(0, 2)
        print(f"Movimiento 1 realizado: {hanoi.torres}")

        # Movimiento 2: Válido
        hanoi.mover_disco(0, 1)
        print(f"Movimiento 2 realizado: {hanoi.torres}")

        # Movimiento 3: Válido
        hanoi.mover_disco(2, 1)
        print(f"Movimiento 3 realizado: {hanoi.torres}")

        # Movimiento 4: No válido (intenta mover desde torre vacía)
        try:
            hanoi.mover_disco(2, 0)
        except ValueError as e:
            print(f"Movimiento no válido (desde torre vacía): {e}")

        # Movimiento 5: No válido (intenta colocar un disco grande sobre uno pequeño)
        try:
            hanoi.mover_disco(0, 1)
        except ValueError as e:
            print(f"Movimiento no válido (disco grande sobre disco pequeño): {e}")

        # Verificar el contador de movimientos válidos
        self.assertEqual(hanoi.movimientos, 3, f"El juego no contó correctamente los movimientos válidos. Contador actual: {hanoi.movimientos}")
        print(f"Prueba completada: Se contó correctamente solo los movimientos válidos ({hanoi.movimientos}).")

if __name__ == "__main__":
    unittest.main()
