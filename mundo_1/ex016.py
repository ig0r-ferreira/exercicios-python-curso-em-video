# Algoritmo que lê um número real qualquer pelo teclado e mostra na tela
# a sua parte inteira, utilizando a biblioteca math.

from math import trunc

num = float(input('Digite um número: ').strip())

print(f'\nO valor digitado foi {num} e a sua parte inteira é {trunc(num)}.')
