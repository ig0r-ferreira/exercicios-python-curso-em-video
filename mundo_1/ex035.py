# Algoritmo que lê o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.


from math import fabs

r1 = float(input('Comprimento da reta 1: ').strip())
r2 = float(input('Comprimento do reta 2: ').strip())
r3 = float(input('Comprimento do reta 3: ').strip())

if (r2 + r3 > r1 > fabs(r2 - r3)) or (r1 + r3 > r2 > fabs(r1 - r3)) or \
        (r1 + r2) > r3 > fabs(r1 - r2):
    print('\nÉ possível formar um triângulo com essas retas.')
else:
    print('\nNão é possível formar um triangulo com essas retas.')
