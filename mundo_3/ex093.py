# Exercício 93 - Indicador de aproveitamento de um jogador v1.0
#
# Programa que gerencia o aproveitamento de um jogador de futebol com base no total de partidas ele
# jogou e a quantidade de gols feitos em cada partida.
# Ao final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o
# campeonato.


print(f'\n{" INDICADOR DE APROVEITAMENTO DO JOGADOR ":=^50}\n')


jogador = {
    'nome': input('Nome do jogador: ').strip().upper(),
    'total_partidas': int(input('Total partidas jogadas: ').strip()),
    'gols_partida': [],
    'total_gols': 0
}


for n in range(1, jogador['total_partidas'] + 1):
    jogador['gols_partida'].append(int(input(f'=> Quantidade de gols na {n}ª partida: ').strip()))

jogador['total_gols'] = sum(jogador['gols_partida'])


print(f'\nO {jogador["nome"]} jogou {jogador["total_partidas"]} partida(s).')

for n, quant in enumerate(jogador['gols_partida']):
    print(f'=> Na {n + 1}ª partida, fez {quant} gol(s).')

print(f'\nAo todo, {jogador["nome"]} fez {jogador["total_gols"]} gol(s).')
