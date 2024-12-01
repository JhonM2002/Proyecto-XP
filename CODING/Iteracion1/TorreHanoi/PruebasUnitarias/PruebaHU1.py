import unittest
from TorreHanoi import TorreHanoi  # Importa la clase TorreHanoi

class TestRepresentacionBasica(unittest.TestCase):
    def test_inicializacion_torres(self):
        """HU1: Verificar que las torres y discos se inicialicen correctamente con un número configurable de discos."""
        print("\nIniciando prueba de inicialización de torres (HU1)...")

        # Configurar el número de discos para la prueba
        num_discos = int(input("Ingresa el número de discos para la prueba HU1: "))
        
        # Inicializar la Torre de Hanoi con el número de discos configurado
        hanoi = TorreHanoi(num_discos)
        estado_esperado = [list(range(num_discos, 0, -1)), [], []]
        
        print(f"Estado inicial esperado: {estado_esperado}")
        print(f"Estado inicial obtenido: {hanoi.torres}")
        
        # Verificar que el estado inicial sea el esperado
        self.assertEqual(hanoi.torres, estado_esperado, "Las torres no se inicializaron correctamente.")
        print("Prueba HU1 completada con éxito: Las torres se inicializaron correctamente.")

if __name__ == "__main__":
    unittest.main()
    