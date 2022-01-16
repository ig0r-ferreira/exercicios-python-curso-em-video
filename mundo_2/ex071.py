# Exercício 71 - Simulador de Caixa Eletrônico
#
# Programa que simula o funcionamento de um caixa eletrônico. No início, pergunta ao usuário
# qual será o valor a ser sacado (número inteiro) e depois informando quantas cédulas de
# cada valor serão entregues.
#
# OBS: Considerando que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print(f'\n{" CAIXA ELETRÔNICO ":-^50}\n')

valor = int(input('Quanto você quer sacar? R$ ').strip())

if 2000 >= valor > 0:
    print('\nVocê receberá:\n')

    cedulas50 = valor // 50
    if cedulas50 > 0:
        print(f'{cedulas50} cédula(s) de R$ 50.')

    cedulas20 = valor % 50 // 20
    if cedulas20 > 0:
        print(f'{cedulas20} cédula(s) de R$ 20.')

    cedulas10 = valor % 50 % 20 // 10
    if cedulas10 > 0:
        print(f'{cedulas10} cédula(s) de R$ 10.')

    cedulas1 = valor % 50 % 20 % 10 // 1
    if cedulas1 > 0:
        print(f'{cedulas1} cédula(s) de R$ 1.')

elif valor > 2000:
    print('\nErro: O valor máximo para saque é de R$ 2000.')

else:
    print('\nErro: Valor inválido! Informe novamente o valor a ser sacado.')
