# Exercício 106 - Interactive Helping System
#
# Mini-sistema que utiliza o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
import time

backgd = {
    'verde': '\033[1;42m',
    'azul': '\033[1;44m',
    'vermelho': '\033[1;41m',
    'inverso': '\033[1;7m',
    'neutro': '\033[m'
}

font = {
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
}

size = 130

print(f'{backgd["verde"]}\n' + ('=' * size))
# print(backgd['verde'] + '\n' + ('=' * size))

titulo_inicial = f'{backgd["neutro"]}{font["verde"]}{backgd["inverso"]}' \
                 f'SISTEMA PYHELP' \
                 f'{backgd["neutro"]}{backgd["verde"]}'

print(f'{titulo_inicial:^{size}}')
print('=' * size, end='\n\n')

while True:
    time.sleep(1)

    print(f'{backgd["neutro"]}{backgd["azul"]}', end='')

    comando = input('* Função ou biblioteca >>>: ').strip().lower()

    if comando == 'fim':
        print(f'{backgd["vermelho"]}\n' + ('=' * size))

        titulo_final = f'{backgd["neutro"]}{font["vermelho"]}{backgd["inverso"]}' \
                       f'SAINDO DO SISTEMA PYHELP...' \
                       f'{backgd["neutro"]}{backgd["vermelho"]}'

        print(f'{titulo_final:^{size}}')
        print('=' * size, end='\n\n')

        time.sleep(1.5)

        break

    print(f'{backgd["neutro"]}{backgd["inverso"]}', end='')

    help(comando)
