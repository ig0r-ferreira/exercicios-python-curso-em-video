# Algoritmo que lê um número inteiro e mostra na tela se ele é PAR ou ÍMPAR.
import sys

num = input('\nDigite um número inteiro: ').strip()

try:
    num = int(num)

    if num % 2 == 0:
        print(f'\n{num} é PAR.')
    else:
        print(f'\n{num} é ÍMPAR.')

except ValueError:
    sys.exit('\nErro: Você não informou um número inteiro!')
