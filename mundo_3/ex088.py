# Exercício 88 - Palpites para MEGA SENA
#
# Programa que ajuda um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.


from time import sleep
from random import randint

jogos = []

print(f'\n{" PALPITES PARA MEGA SENA ":-^100}\n')

while True:
    total_jogos = int(input('Quantos jogos você quer que eu sorteie? ').strip())

    if total_jogos > 0:
        break
    else:
        print('\nVocê deve escolher pelo menos 1 jogo!\n')


print(f'\nSorteando {total_jogos} jogo(s)...\n')

for i in range(1, total_jogos + 1):
    sleep(1.5)
    jogo = []

    for t in range(1, 7):
        palpite = randint(1, 60)

        while palpite in jogo:
            palpite = randint(1, 60)

        jogo.append(palpite)

    jogo = sorted(jogo)
    jogos.append(jogo)

    print(f'Jogo {i}: {jogo}')

print(f'\n{" BOA SORTE NA SUA APOSTA! ":-^100}')
