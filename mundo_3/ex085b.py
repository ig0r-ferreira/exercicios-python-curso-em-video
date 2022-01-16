# Exercício 85 - Matriz com pares e ímpares
#
# Programa no qual o usuário pode digitar sete valores numéricos sendo que o sistema irá cadastrá-los
# em uma lista que contém uma lista com valores pares e outra com os ímpares. Ao final, mostra os
# valores pares e ímpares em ordem crescente.


valores = [[], []]
total = 7

for i in range(1, total + 1):
    valor = int(input(f'{i}º valor: ').strip())
    pos = valor % 2

    valores[pos].append(valor)


print(f'\n{valores}\n')
print(f'Pares: {sorted(valores[0])}')
print(f'Ímpares: {sorted(valores[1])}')
