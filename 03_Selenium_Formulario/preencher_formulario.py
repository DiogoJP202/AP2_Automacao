"""Preenche e envia o formulário local via Selenium. Pausa de 0,8s entre ações."""
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGINA_HTML = Path(__file__).with_name('avaliacao_automacao.html')

def criar_navegador():
    opcoes = Options()
    if os.environ.get('HEADLESS') == '1':
        opcoes.add_argument('--headless=new')
    opcoes.add_argument('--window-size=1440,1120')
    return webdriver.Chrome(options=opcoes)

def pausa():
    time.sleep(0.8)

def preencher_e_enviar(navegador):
    navegador.find_element(By.ID, 'nome').send_keys(os.getenv('ALUNO_NOME', 'Diogo Antonny'))
    pausa()
    navegador.find_element(By.NAME, 'ra').send_keys(os.getenv('ALUNO_RA', '2403813'))
    pausa()
    Select(navegador.find_element(By.ID, 'dia')).select_by_value('16')
    pausa()
    Select(navegador.find_element(By.ID, 'mes')).select_by_value('10')
    pausa()
    Select(navegador.find_element(By.ID, 'ano')).select_by_value('2000')
    pausa()
    Select(navegador.find_element(By.CSS_SELECTOR, '#curso')).select_by_value('ADS')
    pausa()
    Select(navegador.find_element(By.NAME, 'aproveitamento')).select_by_value('9')
    pausa()
    navegador.find_element(By.ID, 'sugestoes').send_keys(
        'Mais desafios práticos com Selenium, testes de API e integração contínua.'
    )
    pausa()
    navegador.find_element(By.NAME, 'observacoes').send_keys(
        'A atividade prática ajudou a entender os localizadores.'
    )
    pausa()
    navegador.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pausa()
    aviso = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, 'feedbackResultado'))
    )
    assert 'Feedback enviado com sucesso' in aviso.text
    print('CONFIRMAÇÃO:', aviso.text)
    return aviso.text

def main():
    navegador = criar_navegador()
    try:
        navegador.get(PAGINA_HTML.resolve().as_uri())
        preencher_e_enviar(navegador)
    finally:
        navegador.quit()

if __name__ == '__main__':
    main()
