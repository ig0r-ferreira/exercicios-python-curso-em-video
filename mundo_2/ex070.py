# Exercício 70 - Estatísticas de produtos
#
# Programa que lê o nome e o preço de vários produtos perguntando a cada produto se o usuário
# vai continuar ou não. Ao final, é mostrado:
#
#   A) Qual é o total gasto na compra.
#
#   B) Quantos produtos custam mais de R$1000.
#
#   C) Qual é o nome do produto mais barato.

print()
print('*' * 100)
print(f'{"CARRINHO - LOJA DESCONTÃO":^100}')
print('*' * 100, end='\n\n')

total_compra = quant_prod_mais1000 = quant_prod = valor_prod_mais_barato = 0
prod_mais_barato = ''
continuar = None

while continuar != 'N':
    print(f'\n{" PRODUTO ":-^50}')

    nome_prod = input('Nome: ').strip().upper()
    valor_prod = float(input('Valor: R$ ').strip())

    total_compra += valor_prod
    quant_prod += 1

    if quant_prod == 1 or valor_prod < valor_prod_mais_barato:
        valor_prod_mais_barato = valor_prod
        prod_mais_barato = nome_prod

    if valor_prod > 1000:
        quant_prod_mais1000 += 1

    print('-' * 50, end='\n')

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()


print('\n')
print('*' * 100)
print(f'O valor total da compra é de R$ {total_compra:.2f}, para {quant_prod} '
      f'produto(s) selecionado(s).')
print(f'Há {quant_prod_mais1000} produto(s) custando mais de 1000 reais.')
print(f'O produto mais barato é {prod_mais_barato} que custa R$ {valor_prod_mais_barato:.2f}.')
print('*' * 100)
