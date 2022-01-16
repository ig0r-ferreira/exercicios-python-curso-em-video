# Algoritmo que pergunta a quantidade de km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado e calcula o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.


km = float(input('Quantos quilômetros(km) rodados? ').strip())
dias = int(input('Por quantos dias foi alugado? ').strip())

valor_aluguel = (60 * dias) + (km * 0.15)

print(f'\nO total a pagar é de R$ {valor_aluguel:.2f}')
