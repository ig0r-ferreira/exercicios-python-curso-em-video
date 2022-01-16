# Exercício 52 - Números primos
#
# Algoritmo que lê um número e informa se ele é primo ou não.


print(f'\n{" Número é primo? ":-^100}')

num = int(input('\nDigite um número inteiro: ').strip())

if num > 1 and (num == 2 or num == 3 or num == 5 or num == 7 or
                not (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0)):
    print(f'\n{num} é um número PRIMO!')

else:
    print(f'\n{num} NÃO É um número PRIMO!')
