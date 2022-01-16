# Exercício 97 - Print especial
#
# Programa que define uma função chamada escreva(), que recebe um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.
# Ex:
#   escreva(‘Olá, Mundo!’)
# Saída:
#   ~~~~~~~~~
#   Olá, Mundo!
#   ~~~~~~~~~


def escreva(texto):
    size = len(texto) + 4
    print('~' * size)
    print(f'{texto:^{size}}')
    print('~' * size)


escreva('APRENDENDO PYTHON')
