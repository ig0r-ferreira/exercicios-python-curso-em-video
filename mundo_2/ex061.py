# Exercício 51 - Progressão Aritmética v2.0
#
# Algoritmo que lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos.


print(f'\n{" Progressão Aritmética v2.0 ":-^100}\n')

a1 = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())

print('\n10 primeiros termos:\n')

n = 0

while n < 10:
    print(a1, end=' ')
    a1 += r
    n += 1

print()
