# Exercício 78 - Maior e menor valores na Lista
#
# Programa que lê 5 valores numéricos e guarda-os em uma lista.
# No final, é mostrado qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.


valores = []

print()

for i in range(0, 5):
    valores.append(int(input('Digite um número: ').strip()))

maior = max(valores)
menor = min(valores)

pos_maior = []
pos_menor = []

for i, v in enumerate(valores):
    if v == maior:
        pos_maior.append(str(i))
    if v == menor:
        pos_menor.append(str(i))

print(f'\nVocê digitou os valores: {", ".join([str(v) for v in valores])}')

print(f'O maior valor digitado é {maior} e se encontra ', end='')
if len(pos_maior) == 1:
    print(f'na posição {pos_maior[0]}.')
else:
    print(f'nas posições {", ".join(pos_maior)}.')

print(f'O menor valor digitado é {menor} e se encontra ', end='')
if len(pos_menor) == 1:
    print(f'na posição {pos_menor[0]}.')
else:
    print(f'nas posições {", ".join(pos_menor)}.')
