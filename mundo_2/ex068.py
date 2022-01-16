# Exercício 68 - Jogo do par ou ímpar
#
# Algoritmo que joga par ou ímpar com o usuário. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint


print(f'\n{" Vamos jogar PAR ou ÍMPAR? ":-^100}\n')
print('\033[1mRegras\033[m: Você só poderá escolher um número de 0 a 5.\n')

vitorias = 0

while True:
    num_usuario = int(input('\nDiga um número: ').strip())

    if 5 >= num_usuario >= 0:
        tipo = ''

        while tipo != 'P' and tipo != 'I':
            tipo = input('PAR [P] ou ÍMPAR [I]? ').strip().upper()

        num_pc = randint(0, 5)

        soma = num_usuario + num_pc

        print(f'\nEu escolhi {num_pc} e você {num_usuario}. Deu {num_pc + num_usuario}, '
              f'valor \033[1m{"PAR" if soma % 2 == 0 else "ÍMPAR"}\033[m.')

        if (tipo == 'P' and soma % 2 == 0) or (tipo == 'I' and soma % 2 != 0):
            print('\nVocê \033[1;32mVENCEU\033[m! Vamos de novo.')
            vitorias += 1
        else:
            print('\nVocê \033[1;31mPERDEU\033[m!')
            break
    else:
        print('\n\033[1;31mErro: Escolha um número de 0 a 5. Tente de novamente!\033[m')


print(f'\n\033[1mFIM DE JOGO\033[m.', end=' ')

if vitorias == 0:
    print('Você não venceu nenhuma vez!')
else:
    print(f'Você venceu {vitorias}x!.')
