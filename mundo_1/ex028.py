# Exercício 28 - Jogo da Adivinhação
#
# Algoritmo que sortea um número inteiro entre 0 e 5 e que pede para o usuário tentar
# descobrir qual foi o número escolhido pelo computador, informando a ele se venceu ou
# perdeu.
import sys
from random import randint
from time import sleep

print('\nEstou pensando em um número de 0 a 5...')
sleep(2)

num_sort = randint(0, 5)

num_usuario = input('\nEm qual número eu pensei? ').strip()

try:
    num_usuario = int(num_usuario)

    if num_usuario == num_sort:
        print('\nParabéns! Você acertou!')
    elif num_usuario < 0 or num_usuario > 5:
        print('\nPassou longe! O número que eu pensei é de 0 a 5.')
    else:
        print(f'\nQue pena! Você errou! Eu pensei no número {num_sort}.')

except ValueError:
    sys.exit('\nErro: Você não digitou um número!')
