# Exercício 100 - Funções para sortear e somar números
#
# Programa que define uma lista chamada números e duas funções chamadas sorteia() e soma_pares().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint
from time import sleep

numeros = []
pares = []


def sortear(quant):
    print(f'\nSorteando {quant} números...')
    sleep(1)

    for i in range(0, quant):
        num = randint(0, 100)

        if num % 2 == 0:
            print(f'\033[1;32m{num}\033[m', end=' ')
            pares.append(num)
        else:
            print(num, end=' ')

        sleep(1)
        numeros.append(num)

    print()


def somar_pares():
    print(f'\nA soma de todos os valores \033[1;32mpares\033[m é {sum(pares)}.')


sortear(5)
somar_pares()
