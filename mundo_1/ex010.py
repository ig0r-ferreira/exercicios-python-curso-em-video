# Algoritmo que lê quanto dinheiro uma pessoa tem na carteira e
# mostra quantos dólares ela pode comprar.

valor = float(input('Quanto você tem na sua carteira? R$ ').strip())

print(f'\nCom R$ {valor:.2f} você pode comprar U$ {(valor / 5.53):.2f}.')
