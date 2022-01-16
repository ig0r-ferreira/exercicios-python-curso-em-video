# Exercício 99 - Função para encontrar o maior valor
#
# Programa que define uma função chamada maior(), que recebe vários parâmetros com valores inteiros.
# O programa irá analisar todos os valores e dizer qual deles é o maior.


from time import sleep


def maior(* valores):
    print(f'\nValores informados: ', end='')
    sleep(1)
    for v in valores:
        print(v, end=' ')
        sleep(1)
    print(f'\nO maior valor é {max(valores)}.')


maior(98, 11, 2)
maior(8, 0, 27, 4, 11, 2)
maior(3, 5, 2, 9)
