# Exercício 108 - Formatando moeda v1.0
#
# Programa que mostra os valores formatados como valores monetários utilizando uma função adicional
# chamada format().


import moeda

valor = float(input('\nDigite um valor: R$ ').strip())

print()
print(f'O dobro de {moeda.formatar(valor)} é {moeda.formatar(moeda.dobro(valor))}.')
print(f'A metade de {moeda.formatar(valor)} é {moeda.formatar(moeda.metade(valor))}.')
print(f'Aumentando em 30%, temos {moeda.formatar(moeda.aumentar(valor, 30))}.')
print(f'Reduzindo em 10%, temos {moeda.formatar(moeda.diminuir(valor, 10))}.')
