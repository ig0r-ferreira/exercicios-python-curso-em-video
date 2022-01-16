# Algoritmo que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou
# iguais, o aumento é de 15%.


salario = float(input('\nQuanto é o seu salário? R$ ').strip())

if salario > 1250.0:
    print(f'\nVocê recebeu um aumento de 10%! Seu novo salário é R$ {salario * 1.1:.2f}')
else:
    print(f'\nVocê recebeu um aumento de 15%! Seu novo salário é R$ {salario * 1.15:.2f}')
