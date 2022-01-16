# Exercício 59 - Operações com dois valores
#
# Algoritmo que lê 2 valores e mostra na tela um menu com as seguintes opções:
#
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair


import time


print(f'\n{" Operações com 2 valores ":-^100}\n')

valor1 = float(input('1º valor: ').strip())
valor2 = float(input('2º valor: ').strip())

menu = '\n\nEscolha uma opção:\n\n' \
       '[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Sair\n'

print(menu)

opcao = 0

while opcao != 5:
    opcao = int(input('\nOpção: ').strip())

    if opcao == 1:
        print(f'{" Soma ":-^50}\n')
        print(f'{valor1} + {valor2} = {valor1 + valor2}')

    elif opcao == 2:
        print(f'{" Multiplicação ":-^50}\n')
        print(f'{valor1} x {valor2} = {(valor1 * valor2):.2f}')

    elif opcao == 3:
        print(f'{" Maior valor ":-^50}\n')

        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior é {valor1}')
        elif valor1 < valor2:
            print(f'Entre {valor1} e {valor2} o maior é {valor2}')
        else:
            print(f'Não há maior valor. {valor1} é igual a {valor2}.')

    elif opcao == 4:
        print(f'{" Novos valores ":-^50}\n')
        valor1 = float(input('1º valor: ').strip())
        valor2 = float(input('2º valor: ').strip())

    elif opcao == 5:
        print('\nFinalizando...')
        time.sleep(1)

    else:
        print('\n\033[1;31mErro: Opção inválida. Tente novamente!\033[m')
