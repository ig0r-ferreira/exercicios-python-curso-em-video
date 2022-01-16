# Algoritmo que lê a largura e a altura de uma parede em metros e
# calcula a área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Altura da parede: ').strip())
largura = float(input('Largura da parede: ').strip())

area = altura * largura
litros_tinta = area / 2

print(f'\nA área da sua parede é de {area:.2f}m².')
print(f'Para pintar, você precisará de {litros_tinta:.1f}l de tinta.')
