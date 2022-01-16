# Exercício 85 - Lista com pares e ímpares
#
# Programa no qual o usuário pode digitar sete valores numéricos sendo que o sistema irá cadastrá-los
# em uma lista única que mantém separados os valores pares e ímpares. Ao final, mostra os valores
# pares e ímpares em ordem crescente.


valores = []
total = 7

print()
for i in range(1, total + 1):
    valor = int(input(f'{i}º valor: ').strip())
    pos = valor % 2

    while pos < len(valores) and valores[pos] is not None:
        pos += 2

    while pos >= len(valores):
        valores.append(None)

    valores[pos] = valor

print(f'\n{valores}\n')
print(f'Pares: {sorted([v for v in valores[0::2] if v is not None])}')
print(f'Ímpares: {sorted([v for v in valores[1::2] if v is not None])}')
