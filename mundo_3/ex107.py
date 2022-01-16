# Exercício 107 - Criando e utilizando o módulo moeda
#
# Programa que utiliza as funções de um módulo chamado moeda.py que foi criado com as seguintes
# funcionalidades: aumentar(), diminuir(), dobro() e metade().


import moeda

valor = float(input('\nDigite um valor: R$ ').strip())

print()
print(f'O dobro de R$ {valor} é R$ {moeda.dobro(valor):.2f}.')
print(f'A metade de R$ {valor} é R$ {moeda.metade(valor):.2f}.')
print(f'Aumentando em 30%, temos R$ {moeda.aumentar(valor, 30):.2f}.')
print(f'Reduzindo em 10%, temos R$ {moeda.diminuir(valor, 10):.2f}.')
