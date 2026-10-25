"""Testes Selenium: campos, opções e envio local."""
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from preencher_formulario import PAGINA_HTML, criar_navegador, preencher_e_enviar

class TestFormulario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.navegador = criar_navegador()
        cls.navegador.get(PAGINA_HTML.resolve().as_uri())

    @classmethod
    def tearDownClass(cls):
        cls.navegador.quit()

    def test_01_campos_requisitados_presentes(self):
        for identificador in ('nome', 'ra', 'dia', 'mes', 'ano', 'curso',
                              'aproveitamento', 'sugestoes', 'observacoes', 'enviarFeedback'):
            with self.subTest(elemento=identificador):
                self.assertTrue(self.navegador.find_element(By.ID, identificador).is_displayed())

    def test_02_opcoes_de_curso_e_nota(self):
        cursos = Select(self.navegador.find_element(By.ID, 'curso'))
        self.assertEqual({op.get_attribute('value') for op in cursos.options}, {'', 'ADS', 'SI'})
        notas = Select(self.navegador.find_element(By.ID, 'aproveitamento'))
        self.assertEqual({int(op.get_attribute('value')) for op in notas.options[1:]}, set(range(11)))

    def test_03_preenchimento_e_envio_sem_banco(self):
        aviso = preencher_e_enviar(self.navegador)
        self.assertIn('Nenhum dado foi armazenado', aviso)

if __name__ == '__main__':
    unittest.main(verbosity=2)
