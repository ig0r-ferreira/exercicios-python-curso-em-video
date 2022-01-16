# Exercício 74 - Maior e menor valores em Tuplas
#
# Programa que gera cinco números aleatórios e coloca em uma tupla.
# Depois disso, mostra a listagem de números gerados e indica o menor e o maior valor
# que estão na tupla.


from random import randint

print(f'\n{" MAIOR E O MENOR DOS NÚMEROS SORTEADOS ":=^80}\n')

numeros_aleatorios = (randint(0, 1000), randint(0, 1000), randint(0, 1000),
                      randint(0, 1000), randint(0, 1000))

print('\nNúmeros sorteados: ', end='')

for num in numeros_aleatorios:
    print(num, end=' ')

print(f'\n\n{max(numeros_aleatorios)} é o MAIOR número.')
print(f'\n{min(numeros_aleatorios)} é o MENOR número.')
