# Exercício 42 - Analisando Triângulos v2.0
#
# Algoritmo que lê o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo e se sim, qual seria o triângulo.


from sys import exit
from math import fabs

print('\nAnálise da formação de um TRIÂNGULO\n')

r1 = float(input('Comprimento da reta 1: ').strip())
r2 = float(input('Comprimento do reta 2: ').strip())
r3 = float(input('Comprimento do reta 3: ').strip())


if r1 <= 0 or r2 <= 0 or r3 <= 0:
    exit('Erro: Os comprimentos de reta devem ser maiores que zero!')


if (r2 + r3 > r1 > fabs(r2 - r3)) or (r1 + r3 > r2 > fabs(r1 - r3)) or \
        (r1 + r2) > r3 > fabs(r1 - r2):
    if r1 != r2 != r3 != r1:
        print('\nÉ possível formar um triângulo ESCALENO com essas retas.')
    elif r1 == r2 == r3:
        print('\nÉ possível formar um triângulo EQUILÁTERO com essas retas.')
    else:
        print('\nÉ possível formar um triângulo ISÓCELES com essas retas.')
else:
    print('\nNão é possível formar um triangulo com essas retas.')
