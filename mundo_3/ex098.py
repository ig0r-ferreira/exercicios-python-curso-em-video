# Exercício 98 - PA utilizando função
#
# Programa que define uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# O programa realiza três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


from sys import exit
from time import sleep


def contador(inicio, fim, razao):
    if razao == 0:
        print('\nO intervalo não pode ser 0!')
        exit(0)

    razao = abs(razao)
    print(f'\nContagem de {inicio} até {fim} de {razao} em {razao}...')

    if inicio > fim:
        razao *= -1
        fim -= 1
    else:
        fim += 1

    for i in range(inicio, fim, razao):
        print(i, end=' ')
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print('\nSua vez de personalizar a sequência!')

ini_seq = int(input('Inicio: ').strip())
fim_seq = int(input('Fim: ').strip())
raz_seq = int(input('Intervalo: ').strip())

contador(ini_seq, fim_seq, raz_seq)
