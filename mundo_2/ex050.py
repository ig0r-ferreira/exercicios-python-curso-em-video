# Exercício 50 - Soma dos pares
#
# Algoritmo que lê 6 números inteiros informados pelo usuário e mostra a soma somente
# dos números que são pares.


print(f'\n{" Soma dos pares ":-^100}!\n')

soma = 0
cont_pares = 0
cont_impares = 0

for i in range(1, 7):
    valor = int(input(f'{i}º valor: ').strip())

    if valor % 2 == 0:
        soma += valor
        cont_pares += 1
    else:
        cont_impares += 1

if cont_impares == 6:
    print('\nNão há valores pares para somar!')
else:
    print(f'\nO total de números PARES é {cont_pares} e a soma deles é igual a {soma}.')
