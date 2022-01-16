# Algoritmo que lê a velocidade de um carro. Se ele ultrapassar 80Km/h, mostra uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('\nDigite a velocidade do seu carro: ').strip())

if velocidade > 80.0:
    print('\nVocê foi multado! Sua velocidade excedeu o limite de 80 km/h.')
    print(f'A multa é de R${(velocidade - 80) * 7:.2f}.')
else:
    print('\nVocê está dentro do limite. Continue assim!')
