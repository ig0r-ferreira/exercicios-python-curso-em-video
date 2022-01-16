# Algoritmo que lê o comprimento dos catetos de um triângulo retângulo e
# calcula o comprimento da hipotenusa, utilizando a biblioteca math.

from math import hypot

cateto_op = float(input('Comprimento do cateto oposto: ').strip())
cateto_adj = float(input('Comprimento do cateto adjacente: ').strip())

print(f'\nO comprimento da hipotenusa é {hypot(cateto_op, cateto_adj):.2f}.')
