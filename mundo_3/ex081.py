# Exercício 81 - Extraindo dados de uma Lista
#
# Programa que lê vários números e coloca em uma lista. Depois disso, mostre:
#
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


numeros = []

while True:
    num = int(input('\n=> Digite um número: ').strip())
    numeros.append(num)

    print()

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break

print(f'\nForam digitados {len(numeros)} números.')
print(f'Lista em ordem decrescente: {sorted(numeros, reverse=True)}.')
print(f'O número 5 {"está" if 5 in numeros else "não está"} presente na lista.')
