# Exercício 63 - Fibonacci
#
# Algoritmo que lê um número 'n' inteiro e mostra na tela os 'n' primeiros termos da
# sequência de Fibonacci
#
# -1 -> 1 -> 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21


print(f'\n{" Fibonacci ":-^100}\n')

n = int(input('Você quer ver quantos termos? ').strip())

a, b, i = 1, 0, 0

print()
while i < n:
    a, b = b, a + b
    print(a, end=' -> ')
    i += 1

print('FIM')
