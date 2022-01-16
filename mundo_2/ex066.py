# Exercício 66 - Quantidade e soma dos valores informados v2.0
#
# Algoritmo que lê números inteiros pelo teclado tendo como condição de parada o valor 999.
# Ao final são mostrados quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o 999).


total = soma = 0

print()

while True:
    num = int(input('Digite um número inteiro [999 para finalizar]: ').strip())
    if num == 999:
        break
    total += 1
    soma += num

if total == 0:
    print('\nNenhum número foi informado.')
elif total == 1:
    print(f'\nFoi informado apenas 1 número e o valor dele é {soma}.')
else:
    print(f'\nForam informados {total} números e a soma entre eles é igual a {soma}.')
