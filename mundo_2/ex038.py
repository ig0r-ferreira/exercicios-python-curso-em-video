# Exercício 38 - Comparando números
#
# Algoritmo que lê dois números inteiros e compara-os mostrando na tela as possíveis
# mensagens:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais


valor1 = int(input('Primeiro valor: ').strip())
valor2 = int(input('Segundo valor: ').strip())

if valor1 > valor2:
    print('\nO primeiro valor e MAIOR!')
elif valor1 == valor2:
    print('\nNão existe valor MAIOR, os dois valores são IGUAIS!')
else:
    print(f'\nO segundo valor é MAIOR!')
