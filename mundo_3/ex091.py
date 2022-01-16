# Exercício 91 - Jogo de dados
#
# Programa no qual 4 jogadores jogam um dado e os resultados são armazenados em um dicionário.
# Ao final, o dicionário em colocado em ordem, sabendo que o vencedor tirou o maior número no dado.


from time import sleep
from random import randint

jogadores = []

print(f'\n{" JOGANDO DADOS ":=^30}')
sleep(1)

for i in range(1, 5):
    print(f'\nJogador {i} arremessou o dado...')
    sleep(2)
    dado = randint(1, 6)
    print(f'Ele tira {dado}.')
    sleep(2)
    jogadores.append({'nome': f'Jogador {i}', 'resultado': dado})


print(f'\n{" RANKING ":=^30}\n')

ranking = sorted(jogadores, key=lambda j: j['resultado'], reverse=True)

for pos, jogador in enumerate(ranking):
    print(f'{pos + 1}º lugar: {jogador["nome"]} - Dado: {jogador["resultado"]}')
