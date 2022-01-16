# Exercício 75 - Analise de dados em Tupla
#
# Programa que lê quatro valores pelo teclado e os guarda em uma tupla.
# No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.


print(f'\n{" ANÁLISE DE QUATRO VALORES ":=^80}\n')

numeros = (int(input('1º valor: ').strip()),
           int(input('2º valor: ').strip()),
           int(input('3º valor: ').strip()),
           int(input('4º valor: ').strip()))

pares = ''

print(f'\nVocê informou os números: {numeros}.')

print(f'\nO número 9 foi informado {numeros.count(9)} vez(es).')

if 3 in numeros:
    print(f'\nA primeira ocorrência do número 3 está na posição {numeros.index(3)}.')
else:
    print('\nO número 3 não foi informado.')

for num in numeros:
    if num % 2 == 0:
        pares += str(num) + ' '

if pares != '':
    print(f'\nNúmeros PARES: {pares}')
else:
    print('\nNão há números PARES.')
