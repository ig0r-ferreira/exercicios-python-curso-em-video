# Exercício 45 - Jokenpô v2.0


import sys
from random import choice
from time import sleep


escolha_usuario = 0


print(f'\n{" Jokenpô v2.0 ":-^50}\n')
print("""
Escolha:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] Terminar brincadeira

""")


while escolha_usuario != 4:

    print('-' * 50)

    escolha_usuario = input('\nQual você escolhe? ').strip()

    if not escolha_usuario.isdigit() or int(escolha_usuario) < 1 or int(escolha_usuario) > 4:
        sys.exit('\nErro: Opção inválida! Escolha uma das opções do menu.\n')

    elif int(escolha_usuario) == 4:
        print('\nFIM DE JOGO!')
        break

    else:
        opcoes = {
            '1': 'Pedra',
            '2': 'Papel',
            '3': 'Tesoura'
        }

        print('\nJO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PÔ!!!')
        sleep(0.5)

        print(f'\nVocê escolheu {opcoes[escolha_usuario]}!')
        escolha_usuario = opcoes[escolha_usuario]

        escolha_pc = choice(list(opcoes.values()))
        print(f'\nEu escolhi {escolha_pc}!')

        sleep(1.5)

        if escolha_usuario == escolha_pc:
            print('\nEmpatamos. Vamos de novo!\n')

        elif escolha_usuario == 'Pedra':
            if escolha_pc == 'Papel':
                print('\nPapel embrulha Pedra. Você PERDEU!\n')
            else:
                print('\nPedra quebra Tesoura. Você VENCEU!\n')

        elif escolha_usuario == 'Papel':
            if escolha_pc == 'Pedra':
                print('\nPapel embrulha Pedra. Você VENCEU!\n')
            else:
                print('\nTesoura corta Papel. Você PERDEU!\n')

        else:
            if escolha_pc == 'Pedra':
                print('\nPedra quebra Tesoura. Você PERDEU!\n')
            else:
                print('\nTesoura corta Papel. Você VENCEU!\n')
        sleep(2)

sleep(1)
