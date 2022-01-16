# Exercício 58 - Jogo da Adivinhação v2.0
#
# Algoritmo que sortea um número inteiro entre 0 e 5 e que pede para o usuário tentar
# descobrir qual foi o número escolhido pelo computador, informando a ele se venceu ou
# perdeu.


from random import randint
from time import sleep


print(f'\n{" Jogo da adivinhação v2.0 ":-^100}')

print('\nEstou pensando em um número de 0 a 10...')
sleep(2)

num_sort = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    num_usuario = input('\nEm qual número eu pensei? ').strip()

    try:
        num_usuario = int(num_usuario)

        if 0 <= num_usuario <= 10:
            if num_usuario < num_sort:
                print(f'\nMAIS! Tente outra vez!')
            elif num_usuario > num_sort:
                print(f'\nMENOS! Tente outra vez!')
            else:
                acertou = True
        else:
            print('\n\033[1;31mErro: Você tem que escolher um número de 0 a 10.\033[m')

        tentativas += 1

    except ValueError:
        print('\n\033[1;31mErro: Você não digitou um número!\033[m')

print(f'\nParabéns! Você acertou na sua {tentativas}ª tentativa!')
