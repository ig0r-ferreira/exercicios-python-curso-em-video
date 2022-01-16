# Exercício 60 -  Fatorial
#
# Algoritmo que lê um número qualquer e mostra o seu fatorial


print(f'\n{" Fatorial ":-^100}\n')

num = int(input('Digite um número: ').strip())

fatorial, i = 1, num

print(f'\n{num}! = ', end='')

while i > 0:

    print(i, 'x ' if i > 1 else '= ', end='')

    fatorial *= i
    i -= 1

print(f'{fatorial}.')
