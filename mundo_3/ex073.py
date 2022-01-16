# Exercício 73 - Tuplas com Times de Futebos
#
# Programa que usa uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol em 26/10/2021, para mostrar:
#
#     a) Os 5 primeiros times.
#
#     b) Os últimos 4 colocados.
#
#     c) Times em ordem alfabética.
#
#     d) Em que posição está o time da Chapecoense.


times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Internacional',
         'Corinthians', 'Fluminense', 'Atlético-GO', 'America-MG', 'Cuiabá', 'Athletico-PR',
         'São Paulo', 'Ceará SC', 'Bahia', 'Juventude', 'Santos', 'Sport Recife', 'Grêmio',
         'Chapecoense')


print(f'\n{" BRASILEIRÃO SÉRIE A - 26/10/2021 ":=^100}')

print(f'\n5 primeiros colocados:\n{times[0:5]}')
print(f'\n4 últimos colocados:\n{times[-4:]}')
print('\nEm ordem alfabética:\n' + '\n'.join(sorted(times)))
print(f'\nO time da Chapecoense está na {times.index("Chapecoense") + 1} ª colocação.')

