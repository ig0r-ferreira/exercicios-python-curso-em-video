# Exercício 84 - Lista composta e análise de dados
#
# Programa que lê o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


pessoas = []


while True:
    print(f'\n{f" Pessoa {len(pessoas) + 1} ":-^30}\n')

    dados_pessoa = []

    nome = input('Nome: ').strip().upper()
    peso = float(input('Peso: ').strip())

    dados_pessoa.append(nome)
    dados_pessoa.append(peso)

    pessoas.append(dados_pessoa)

    print()

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break


pessoas_mais_pesadas = []
pessoas_mais_leves = []

maior_peso = max(pessoas, key=lambda p: p[1])[1]
menor_peso = min(pessoas, key=lambda p: p[1])[1]

for pessoa in pessoas:
    # Monta uma lista com o nome das pessoas mais pesadas
    if pessoa[1] == maior_peso:
        pessoas_mais_pesadas.append(pessoa[0])
    # Monta uma lista com o nome das pessoas mais leves
    if pessoa[1] == menor_peso:
        pessoas_mais_leves.append(pessoa[0])


print(f'\nForam cadastradas {len(pessoas)} pessoa(s).')

if len(pessoas_mais_pesadas) > 1:
    print(f'As pessoas mais pesadas são {", ".join(pessoas_mais_pesadas)}, '
          f'que pesam {maior_peso:.1f}kg.')
else:
    print(f'A pessoa mais pesada é {pessoas_mais_pesadas[0]}, que pesa {maior_peso:.1f}kg.')

if len(pessoas_mais_leves) > 1:
    print(f'As pessoas mais leves são {", ".join(pessoas_mais_leves)}, '
          f'que pesam {menor_peso:.1f}kg.')
else:
    print(f'A pessoa mais leve é {pessoas_mais_leves[0]}, que pesa {menor_peso:.1f}kg.')
