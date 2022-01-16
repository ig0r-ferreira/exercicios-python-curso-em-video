# Exercício 93 - Indicador de aproveitamento de um jogador v2.0
#
# Programa que gerencia o aproveitamento de um time de futebol. Coletando para cada jogador,
# o total de partidas ele jogou e a quantidade de gols feitos em cada partida.
# Ao final, o aproveitamento do time e de cada jogador que o usuário selecionar.


from time import sleep


print(f'\n{" INDICADOR DE APROVEITAMENTO DO TIME ":=^75}')

time = []

while True:
    jogador = {
        'nome': input('\nNome do jogador: ').strip().upper(),
        'total_partidas': int(input('Total partidas jogadas: ').strip()),
        'gols_partida': [],
        'total_gols': 0
    }

    for n in range(1, jogador['total_partidas'] + 1):
        jogador['gols_partida'].append(int(input(f'=> Quantidade de gols na {n}ª partida: ').strip()))

    jogador['total_gols'] = sum(jogador['gols_partida'])

    time.append(jogador)

    print()

    while True:
        continuar = input('* Deseja continuar [S/N]? ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break


print(f'\n\n{" TIME ":=^75}\n')
print(f'{"ID":^5}' + ('\t' * 2) + f'{"Jogador":30}' + ('\t' * 5) + f'{"Total de gols"}')
for i, jogador in enumerate(time):
    print(f'{i + 1:^5}' + ('\t' * 2) + f'{jogador["nome"]:30}' + ('\t' * 5) +
          f'{jogador["total_gols"]:^13}')


while True:
    id_jogador = int(input('\n=> Deseja ver, em detalhes, o desempenho de qual jogador? '
                           '[0 para sair] : ').strip())

    if id_jogador == 0:
        print('\nFINALIZANDO O PROGRAMA...')
        sleep(1)
        break
    elif id_jogador < 0 or id_jogador > len(time):
        print('\nERRO! Não existe um jogador com esse ID. Tente novamente.')
    else:
        id_jogador -= 1

        print(f'\nO {time[id_jogador]["nome"]} jogou '
              f'{time[id_jogador]["total_partidas"]} partida(s).')

        for n, quant in enumerate(time[id_jogador]['gols_partida']):
            print(f'=> Na {n + 1}ª partida, fez {quant} gol(s).')

        print(f'\nAo todo, {time[id_jogador]["nome"]} fez '
              f'{time[id_jogador]["total_gols"]} gol(s).')
