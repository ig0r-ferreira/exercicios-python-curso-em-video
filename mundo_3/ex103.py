# Exercício 103 - Ficha do Jogador
#
# Programa que define uma função chamada ficha(), que recebe dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa mostra a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='<desconhecido>', gols=0):
    print(f'\nO jogador {nome} marcou {gols} gol(s) no campeonato.')


print(f'\n{" FICHA DO JOGADOR ":=^45}\n')

nome_jogador = input('Nome do jogador: ').strip()
total_gols = input('Total de gols: ').strip()

if nome_jogador.isalpha():
    if total_gols.isnumeric():
        ficha(nome_jogador, int(total_gols))
    else:
        ficha(nome_jogador)
else:
    if total_gols.isnumeric():
        ficha(gols=int(total_gols))
    else:
        ficha()
