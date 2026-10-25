"""Arquivo solicitado pelo professor: tests/test_funcao.py."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from calculadora import somar

class TestFuncaoSoma(unittest.TestCase):
    def test_soma_exemplo_do_enunciado(self):
        self.assertEqual(somar(5, 2), 7)
    def test_soma_com_zero(self):
        self.assertEqual(somar(0, 0), 0)
    def test_soma_com_negativos(self):
        self.assertEqual(somar(-3, 2), -1)
    def test_soma_com_valor_negativo(self):
        self.assertEqual(somar(10, -4), 6)

if __name__ == "__main__":
    unittest.main(verbosity=2)
