# Exercício 109 - Formatando moeda v2.0
#
# Programa que testa as funçoes do módulo moeda que foram adaptadas para receber um parâmetro a mais,
# que irá indicar se o valor retornado por elas vai ser ou não formatado pela função format().


import moeda

valor = float(input('\nDigite um valor: R$ ').strip())

print()
print(f'O dobro de {moeda.formatar(valor)} é {moeda.dobro(valor, fmtd=True)}.')
print(f'A metade de {moeda.formatar(valor)} é {moeda.metade(valor, fmtd=True)}.')
print(f'Aumentando em 30%, temos {moeda.aumentar(valor, 30, fmtd=True)}.')
print(f'Reduzindo em 10%, temos {moeda.diminuir(valor, 10, fmtd=True)}.')
