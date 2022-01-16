# Exercício 55 - Quem tem maior e menor peso
#
# Algoritmo que lê o peso de 5 pessoas e mostra qual foi maior e o menor pesso.


print(f'\n{" Maior e menor peso ":-^100}\n')

peso_min = 0
peso_max = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: ').strip())

    if i == 1 or peso > peso_max:
        peso_max = peso

    if i == 1 or peso < peso_min:
        peso_min = peso

print(f'\nO maior peso é {peso_max:.1f} kg.')
print(f'\nO menor peso é {peso_min:.1f} kg.')
