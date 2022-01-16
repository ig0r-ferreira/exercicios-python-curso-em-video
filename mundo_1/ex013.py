# Algoritmo que lê o salário de um funcionário e mostra seu novo salário, com 15% de aumento.

salario = float(input('Informe o seu salário: R$ '))

print(f'\nVocê recebeu um aumento de 15%!\n'
      f'Seu novo salário é de R$ {salario * 1.15:.2f}.')
