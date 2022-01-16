# Exercício 87 - Matriz 3 x 3 - v2.0
#
# Aprimore o desafio anterior, mostrando no final:
#
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[], [], []]
maior = maior_linha2 = soma_pares = soma_coluna3 = 0

print()

for linha in range(1, 4):
    for coluna in range(1, 4):
        valor = int(input(f'Digite o valor da posição [{linha}][{coluna}]: ').strip())

        if linha == 1 and coluna == 1 or valor > maior:
            maior = valor

        # Realiza a soma dos valores pares
        if valor % 2 == 0:
            soma_pares += valor

        # Realiza a soma da coluna 3
        if coluna == 3:
            soma_coluna3 += valor

        # Calcula o maior valor da linha 2
        if linha == 2 and (coluna == 1 or valor > maior_linha2):
            maior_linha2 = valor

        matriz[linha - 1].append(valor)

print(f'\n{" Matriz 3 x 3 ":-^37}\n')

for linha in range(0, 3):

    size = str(len(str(maior)))

    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^{size}}]', end='\t')

    print()

print(f'\nA soma de todos os valores pares é igual a {soma_pares}.')
print(f'A soma de todos os valores da 3ª coluna é igual a {soma_coluna3}.')
print(f'O maior valor da 2ª linha é {maior_linha2}.')
