import unittest
from TorreHanoi import TorreHanoi

class TestMovimientoValido(unittest.TestCase):
    def test_movimiento_valido(self):
        """HU2: Verifica que se pueda mover un disco válido entre torres."""
        print("\nIniciando prueba: Movimiento válido (HU2)")
        hanoi = TorreHanoi(3)
        print(f"Estado inicial de las torres: {hanoi.torres}")

        hanoi.mover_disco(0, 2)  # Mueve el disco más pequeño de la Torre 1 a la Torre 3
        print(f"Movimiento realizado de Torre 1 a Torre 3: {hanoi.torres}")

        self.assertEqual(hanoi.torres, [[3, 2], [], [1]], "El movimiento válido no actualizó correctamente las torres.")
        print("Prueba completada: Movimiento válido realizado con éxito.")

if __name__ == "__main__":
    unittest.main()
