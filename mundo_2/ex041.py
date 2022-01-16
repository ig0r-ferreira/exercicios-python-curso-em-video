# Exercício 41 - Classificando atletas
#
# A Confederação Nacional de Natação precisa de um algoritmo que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER


from datetime import date

nome = input('\nNome do atleta: ').strip()
ano_nasc = int(input('Ano de nascimento: ').strip())

idade = date.today().year - ano_nasc

if idade <= 9:
    print(f'\nO atleta {nome} compõe a categoria MIRIM!')
elif idade <= 14:
    print(f'\nO atleta {nome} compõe a categoria INFANTIL!')
elif idade <= 19:
    print(f'\nO atleta {nome} compõe a categoria JÚNIOR!')
elif idade <= 25:
    print(f'\nO atleta {nome} compõe a categoria SÊNIOR!')
else:
    print(f'\nO atleta {nome} compõe a categoria MASTER!')
