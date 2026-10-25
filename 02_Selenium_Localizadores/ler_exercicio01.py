"""Atende itens a, b e c: abrir HTML local e mostrar título + dois localizadores."""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

CAMINHO_HTML = Path(__file__).with_name("exercicio01.html")

def criar_navegador():
    opcoes = Options()
    if os.environ.get("HEADLESS") == "1":
        opcoes.add_argument("--headless=new")
    return webdriver.Chrome(options=opcoes)

def executar():
    navegador = criar_navegador()
    try:
        navegador.get(CAMINHO_HTML.resolve().as_uri())
        print("a) Título da página:", navegador.title)
        elemento_tag = navegador.find_element(By.TAG_NAME, "p")
        print("b) Parágrafo por TAG_NAME:", elemento_tag.text)
        elemento_css = navegador.find_element(By.CSS_SELECTOR, "p.content")
        print("c) Parágrafo por CSS_SELECTOR:", elemento_css.text)
    finally:
        navegador.quit()

if __name__ == "__main__":
    executar()
