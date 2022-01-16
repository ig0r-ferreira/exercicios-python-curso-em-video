# Exercício 45 - Jokenpô


from random import choice
from sys import exit
from time import sleep


print(f'\n{" Jokenpô ":-^50}')


escolha_usuario = input("""
Escolha:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura

Opção: """).strip()


# Se o usuário nao escolheu um valor dentro do intervalo informado mostra a mensagem
# de opção inválida
if not escolha_usuario.isdigit() or int(escolha_usuario) < 1 or int(escolha_usuario) > 3:
    exit('\nErro: Opção inválida! Tente de novo.')

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

escolha_usuario = opcoes[escolha_usuario]
print(f'\nVocê escolheu {escolha_usuario}!')

escolha_pc = choice(list(opcoes.values()))
print(f'\nEu escolhi {escolha_pc}!')

sleep(1.5)

if escolha_usuario == escolha_pc:
    print('\nEmpatamos! Vamos de novo!')

elif escolha_usuario == 'Pedra':
    if escolha_pc == 'Tesoura':
        print('\nVocê GANHOU! Pedra quebra Tesoura.')
    else:
        print('\nVocê PERDEU! Papel embrulha Pedra.')

elif escolha_usuario == 'Papel':
    if escolha_pc == 'Tesoura':
        print('\nVocê PERDEU! Tesoura corta Papel.')
    else:
        print('\nVocê GANHOU! Papel embrulha Pedra.')

else:
    if escolha_pc == 'Pedra':
        print('\nVocê PERDEU! Pedra quebra Tesoura.')
    else:
        print('\nVocê GANHOU! Tesoura corta Papel.')
