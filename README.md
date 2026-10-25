# AP2 — Automação de Testes de Software

**Nome:** Diogo Antonny Santos Soares 
**RA:** 2403813  
**Disciplina:** Automação de Testes de Software

## Estrutura das atividades

| Exercício | Diretório | O que foi resolvido |
|---|---|---|
| 01 — Doublés de teste | `01_Doubles/` | `Stub`, `Spy`, serviço e testes `unittest` |
| Bora Praticar 02 | `02_Selenium_Localizadores/` | HTML local, título, `By.TAG_NAME`, `By.CSS_SELECTOR` e testes |
| Bora Praticar 03 | `03_Selenium_Formulario/` | Formulário HTML autoral, preenchimento Selenium, pausas de `time.sleep(0.8)` e testes |
| 04 — Behave | `04_Behave/` | Função de soma, cenários Gherkin, steps e `tests/test_funcao.py` |

## Preparação

Requisitos: Python 3.10+ e Google Chrome. Instale as dependências na pasta raiz:

```bash
python -m pip install -r requirements.txt
```

## Execução por atividade

Execute os comandos de dentro da pasta correspondente:

```bash
cd 01_Doubles
python -m unittest -v test_agendamento.py
cd ..
```

```bash
cd 02_Selenium_Localizadores
python ler_exercicio01.py
python -m unittest -v test_exercicio01.py
cd ..
```

```bash
cd 03_Selenium_Formulario
python preencher_formulario.py
python -m unittest -v test_formulario.py
cd ..
```

```bash
cd 04_Behave
python -m behave
python -m unittest -v tests/test_funcao.py
cd ..
```
