import unittest
from TorreHanoi import TorreHanoi

class TestVerificarVictoria(unittest.TestCase):
    def test_victoria(self):
        """Verifica que el juego detecte correctamente la victoria."""
        print("\nIniciando prueba: Verificar victoria")
        hanoi = TorreHanoi(3)
        hanoi.torres = [[], [], [3, 2, 1]]  # Simula el estado de victoria
        print(f"Estado de las torres: {hanoi.torres}")
        self.assertTrue(hanoi.verificar_victoria(), "El juego no detectó correctamente la victoria.")
        print("Prueba completada: La victoria fue detectada correctamente.")

if __name__ == "__main__":
    unittest.main()
