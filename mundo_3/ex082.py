# Exercício 82 - Dividindo valores em várias listas
#
# Programa que lê vários números e coloca em uma lista. Depois disso, cria duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


numeros = []
pares = []
impares = []

while True:
    num = int(input('\n=> Digite um número: ').strip())
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    print()

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break

print(f'\nNúmeros digitados: {numeros}.')
print(f'Números pares: {pares}.')
print(f'Números ímpares: {impares}.')
