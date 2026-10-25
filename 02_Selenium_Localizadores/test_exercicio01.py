import unittest
from selenium.webdriver.common.by import By
from ler_exercicio01 import CAMINHO_HTML, criar_navegador

class TestExercicio01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.navegador = criar_navegador()
        cls.navegador.get(CAMINHO_HTML.resolve().as_uri())

    @classmethod
    def tearDownClass(cls):
        cls.navegador.quit()

    def test_titulo_da_pagina(self):
        self.assertEqual(self.navegador.title, "Exercício 01")

    def test_paragrafo_por_tag_name(self):
        paragrafo = self.navegador.find_element(By.TAG_NAME, "p")
        self.assertEqual(paragrafo.text, "O conteúdo do site vem aqui")

    def test_paragrafo_por_css_selector(self):
        paragrafo = self.navegador.find_element(By.CSS_SELECTOR, "p.content")
        self.assertEqual(paragrafo.text, "O conteúdo do site vem aqui")
        self.assertEqual(paragrafo.get_attribute("class"), "content")

if __name__ == "__main__":
    unittest.main(verbosity=2)
