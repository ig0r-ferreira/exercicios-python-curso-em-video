# Algoritmo que lê um ângulo qualquer e mostra na tela o valor do seno, cosseno e
# tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: ').strip())

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nO seno de {angulo}° é {seno:.2f}.')
print(f'O cosseno de {angulo}° é {cosseno:.2f}.')
print(f'A tangente de {angulo}° é {tangente:.2f}.')
