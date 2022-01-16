# Exercício 96 - Cálculo de área com função
#
# Programa que define uma função chamada área(), que recebe as dimensões de um terreno retangular
# (largura e comprimento) e mostra a área do terreno.


def area(comprimento, largura):
    return comprimento * largura


print('=' * 45)
print('\t' * 3, 'CÁLCULO DA ÁREA', '\t' * 3)
print('=' * 45, end='\n\n')

comp = float(input('Comprimento (m): ').strip())
larg = float(input('Largura (m): ').strip())

area = area(comp, larg)

print(f'\nA área de um terreno de {comp}m x {larg}m é de {area:.2f}m².')
