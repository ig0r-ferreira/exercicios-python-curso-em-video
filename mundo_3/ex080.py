# Exercício 80 - Lista ordenada sem repetições
#
# Programa no qual o usuário digita cinco valores numéricos e armazena-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). Ao final, mostra a lista ordenada na tela.


valores = []

for i in range(0, 5):
    valor = int(input('\n=> Digite um valor: ').strip())

    if valor not in valores:

        if i == 0 or valor > valores[-1]:
            valores.append(valor)
            print('Valor adicionado ao final da lista.')
        else:
            pos = 0

            for num in valores:
                if valor > num:
                    pos = valores.index(num) + 1
                else:
                    break

            valores.insert(pos, valor)
            print(f'Valor adicionado a posição {pos}.')
    else:
        print('Esse valor já existe! Ele não será adicionado.')

print(f'\n{valores}')
