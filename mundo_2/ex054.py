# Exercício 54 - Detector de maioridade
#
# Algoritmo que lê o ano de nascimento de 7 pessoas e mostra as que atigiram a maioridade e
# as que ainda não.


from datetime import date


print(f'\n{"Detector de maioridade":-^100}\n')

total_maiores = 0
total_menores = 0

for i in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da pessoa {i}: ').strip())
    ano_atual = date.today().year

    idade = ano_atual - ano_nasc

    if idade >= 18:
        total_maiores += 1
    else:
        total_menores += 1

print(f'\n{total_maiores} pessoa(s) são MAIORES de idade.')
print(f'\n{total_menores} pessoa(s) são MENORES de idade. ')
