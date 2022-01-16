# Exercício 79 - Valores únicos em uma Lista
#
# Programa onde o usuário pode digitar vários valores numéricos que serão armazenados em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


valores = []

while True:

    valor = int(input('\n=> Digite um valor: ').strip())

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existe na lista! Ele não será adicionado.')

    print()

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break

print(f'\nValores adicionados: {sorted(valores)}')
