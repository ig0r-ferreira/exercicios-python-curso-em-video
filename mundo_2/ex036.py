# Exercício 36 - Aprovando empréstimo
#
# Algoritmo que aprova o empréstimo bancário para a compra de uma casa.
#
# Informações solicitadas:
# - Valor da casa
# - Salário do comprador
# - Quantos anos ele vai pagar
#
# Condição:
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


from time import sleep

valor_casa = float(input('\nQual é o valor da casa que você deseja comprar? R$ ').strip())
salario = float(input('Quanto você ganha? R$ ').strip())
anos_financ = int(input('Por quantos anos será o financiamento? ').strip())

prestacao = valor_casa / (anos_financ * 12)

print('\nAguarde alguns instantes...')
sleep(2)
print('Estamos analisando as suas informações...')
sleep(4)

# Se o valor da prestação é maior que 30% do salário informa que o empréstimo foi negado
if prestacao > (salario * 0.3):
    print('\nInfelizmente, o empréstimo que você solicitou foi negado!'
          '\nAnalisamos a sua renda e o valor do imóvel e entendemos que você não tem '
          '\ncondições de pagar as prestações no período solicitado.')

# Caso contrário, informa que o empréstimo foi aprovado
else:
    print(f'\nA sua solicitação de empréstimo foi aprovada!'
          f'\nO pagamento será de {(anos_financ * 12)}x de R$ {prestacao:.2f}.'
          f'\nEstamos felizes em poder ajudar com a realização do seu sonho. '
          f'Faça bom proveito!')
