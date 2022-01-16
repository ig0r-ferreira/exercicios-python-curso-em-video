# Exercício 51 - Progressão Aritmética
#
# Algoritmo que lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos.


print(f'\n{" Progressão Aritmética ":-^100}\n')

a1 = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())

print('\n10 primeiros termos:\n')

a10 = a1 + (10 - 1) * r

for an in range(a1, a10 + r, r):
    print(an)
