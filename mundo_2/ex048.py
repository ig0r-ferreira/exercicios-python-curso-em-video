# Exercício 48 - Soma dos ímpares múltiplos de 3 que estão entre 1 e 500
#
# Algoritmo que calcula a soma de todos os números ímpares que são múltiplos de 3 e
# que estão entre 1 e 500


soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'\nA soma de todos os números ímpares entre 1 e 500 e que são múltiplos de 3 '
      f'é igual a {soma}.')
