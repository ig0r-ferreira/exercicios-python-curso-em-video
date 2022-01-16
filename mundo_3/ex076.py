# Exercício 76 - Lista de preços com Tuplas
#
# Programa que tem uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência e no final, mostra uma listagem de preços, organizando os dados em forma
# tabular.


tabela = ('Televisão', 1700, 'Ventilador', 119.99, 'Notebook', 3569.99,
          'Sofá', 1000, 'Bicicleta', 749.99, 'Headset', 125.50)


print(f'\n{" LISTAGEM DE PREÇOS ":=^50}\n')


for i in range(0, len(tabela), 2):
    print(f'{tabela[i]+" ":.<30}', end=' ')
    print(f'R$ {tabela[i + 1]:.2f}')
