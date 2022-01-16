# Exercício 43 - Índice de Massa Corporal (IMC)
#
# Algoritmo que lê o peso e a altura de uma pessoa, e calcula seu IMC mostrando seu status,
# de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida


print('\nCalculando o IMC\n')

altura = float(input('Sua altura (m): ').strip())
peso = float(input('Seu peso (kg): ').strip())

imc = peso / altura ** 2

print(f'\nSeu IMC é igual a {imc:.1f}kg/m².', end=' ')

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc < 25:
    print('Você está no peso IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
