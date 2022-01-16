# Exercício 86 - Matriz 3x3
#
# Programa que declara uma matriz de dimensão 3×3 e preenche com valores lidos pelo teclado. Ao final,
# mostra a matriz na tela, com a formatação correta.


matriz = [[], [], []]
maior = 0

print()

for linha in range(1, 4):
    for coluna in range(1, 4):
        valor = int(input(f'Digite o valor da posição [{linha}][{coluna}]: ').strip())

        if linha == 1 and coluna == 1 or valor > maior:
            maior = valor

        matriz[linha - 1].append(valor)

print(f'\n{" Matriz 3 x 3 ":-^37}\n')

for linha in range(0, 3):

    size = str(len(str(maior)))

    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^{size}}]', end='\t')

    print()
