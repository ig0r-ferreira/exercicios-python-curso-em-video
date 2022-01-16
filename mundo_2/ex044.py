# Exercício 44 - Gerenciador de Pagamentos
#
# Algoritmo que calcula o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros


valor_prod = float(input('Preço do produto: R$ ').strip())
cond_pag = int(input("""
Condição de pagamento:
[ 1 ] Dinheiro/Cheque
[ 2 ] Cartão

Opção: """).strip())

if cond_pag == 1:
    # Valor do produto com 10% de desconto
    valor_prod = valor_prod * 0.9

    print(f'\nFoi aplicado um desconto de 10% à sua compra. '
          f'O valor a ser pago é de R$ {valor_prod * 0.9:.2f}.')

elif cond_pag == 2:

    quant_parcelas = int(input('Quantidade de parcelas: ').strip())

    if quant_parcelas <= 0 or quant_parcelas > 12:
        print('\nQuantidade de parcelas inválida. Você só pode parcelar até 12x!')

    elif quant_parcelas == 1:
        # Valor do produto com 5% de desconto
        valor_prod = valor_prod * 0.95

        print(f'\nFoi aplicado um desconto de 5% à sua compra. '
              f'O valor a ser pago é de R$ {valor_prod:.2f}.')

    elif quant_parcelas == 2:
        print(f'\nA sua compra foi parcelada em {quant_parcelas}x de '
              f'R$ {valor_prod / quant_parcelas:.2f}.')

    else:
        # Valor do produto com acréscimo de 20% de juros
        valor_prod = valor_prod * 1.2

        print(f'\nA sua compra foi parcelada em {quant_parcelas}x de '
              f'R$ {valor_prod / quant_parcelas:.2f} com aplicação de 20% de juros.')
else:
    print('\nInforme se é no dinheiro/cheque ou cartão!')
