# Algoritmo que lê um número e mostra o dobro, o triplo e a raiz quadrada.

num = int(input('Digite um número: ').strip())

print(f'\nO dobro é {num * 2}.')
print(f'O triplo é {num * 3}.')
print(f'A raiz quadrada é {num ** (1 / 2):.2f}.')
