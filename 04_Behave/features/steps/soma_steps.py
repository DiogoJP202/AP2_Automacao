"""Definições de steps usadas por python -m behave."""
from behave import given, when, then
from calculadora import somar

@given("primeiro valor sera {valor:d}")
def passo_primeiro_valor(context, valor):
    context.primeiro = valor

@given("segundo valor sera {valor:d}")
def passo_segundo_valor(context, valor):
    context.segundo = valor

@when("executa a funcao")
def passo_executar_funcao(context):
    context.resultado = somar(context.primeiro, context.segundo)

@then("saida devera ser o valor {esperado:d}")
def passo_verificar_resultado(context, esperado):
    assert context.resultado == esperado, (
        f"Esperado: {esperado}, recebido: {context.resultado}"
    )
