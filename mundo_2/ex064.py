# Exercício 64 - Quantidade e soma dos valores informados
#
# Algoritmo que lê vários números inteiros informados pelo usuário enquanto ele não
# digitar 999. Ao final é mostrado a quantidade de números digitados e a soma entre eles.


cont = soma = num = 0

print()

while num != 999:
    num = int(input('Informe um número [999 para parar]: ').strip())

    if num != 999:
        soma += num
        cont += 1

print(f'\nForam informados {cont} números e a soma deles é igual a {soma}.')
