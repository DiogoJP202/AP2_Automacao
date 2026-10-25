Feature: soma
  Como estudante de automacao de testes
  Quero validar uma funcao de soma com cenarios em Gherkin
  Para confirmar resultados esperados

  Scenario: Soma dois numeros
    Given primeiro valor sera 5
    And segundo valor sera 2
    When executa a funcao
    Then saida devera ser o valor 7

  Scenario Outline: Soma com valores diversos
    Given primeiro valor sera <primeiro>
    And segundo valor sera <segundo>
    When executa a funcao
    Then saida devera ser o valor <resultado>

    Examples:
      | primeiro | segundo | resultado |
      | 0        | 0       | 0         |
      | -3       | 2       | -1        |
      | 10       | -4      | 6         |
