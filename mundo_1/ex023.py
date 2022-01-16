# Algoritmo que lê um número de 0 a 9999 e mostra na tela cada um dos dígitos separados.


import sys

num = input('Digite um valor entre 0 e 9999: ').strip()

try:
    num = int(num)

    if num <= 0 or num >= 9999:
        sys.exit('\nErro: O valor não está dentro do intervalo informado!')

    unidade = num // 1 % 10
    dezena = num // 10 % 10
    centena = num // 100 % 10
    milhar = num // 1000 % 10

    print(f'\nUnidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhar: {milhar}')

except ValueError:
    sys.exit('\nErro: Você não digitou um valor!')
