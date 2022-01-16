# Algoritmo que pergunta a distância de uma viagem em Km e calcula o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.


distancia = float(input('\nQual é a distância, em km, da viagem? ').strip())
valor_passagem = 0

if distancia <= 200:
    valor_passagem = distancia * 0.5
else:
    valor_passagem = distancia * 0.45

print(f'\nA passagem custa R${valor_passagem:.2f}.')
