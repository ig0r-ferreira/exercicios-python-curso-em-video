# Exercício 51 - Progressão Aritmética v3.0
#
# Algoritmo que lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos.


print(f'\n{" Progressão Aritmética v2.0 ":-^100}\n')

a1 = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())

print('\n10 primeiros termos:\n')

n, i = 10, 1

while i <= n:
    print(a1, end=' ')

    if i == n:
        n += int(input('\n\nVocê quer que mostre mais quantos termos? ').strip())
        print()

    a1 += r
    i += 1

print(f'Total de termos mostrados: {n}')
