# Algoritmo que lê o preço de um produto e mostra seu novo preço, com 5% de desconto.

valor_prod = float(input('Qual é o preço do produto? R$ ').strip())

print(f'\nSeu produto que custava R$ {valor_prod:.2f}, '
      f'com 5% de desconto custa R$ {valor_prod * 0.95 :.2f}.')
