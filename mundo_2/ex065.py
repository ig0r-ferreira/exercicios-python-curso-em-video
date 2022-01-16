# Exercicio 65 - Cálculo da média e do maior e menor número informado
#
# Algoritmo que lê vários números inteiros enquanto o usuário informar que quer continuar
# a digitar. Ao final é mostrado a média dos valores informados e qual é o maior e menor
# valor.


maior = menor = soma = quant = 0
continuar = 'S'


while continuar == 'S':
    num = int(input('\nInforme um número: ').strip())

    if quant == 0 or num > maior:
        maior = num
    if quant == 0 or num < menor:
        menor = num

    soma += num
    quant += 1

    continuar = ''

    while continuar != 'S' and continuar != 'N':
        continuar = input('\n- Deseja continuar [S/N]? ').strip().upper()

print(f'\nA média dos valores informados é {(soma / quant):.2f}.')
print(f'O maior valor é {maior} e o menor é {menor}.')
