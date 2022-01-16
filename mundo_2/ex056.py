# Exercício 56 - Analisando um grupo de pessoas
#
# Algoritmo que lê o nome, a idade e o sexo de 4 pessoas e mostra:
#
# - A média de idade do grupo
# - Qual é nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos


print(f'\n{" Analisando um grupo de 4 pessoas ":-^100}')

total_pessoas = 4
soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
total_mulheres_menor_20 = 0

for i in range(1, total_pessoas + 1):
    nome = input(f'\nNome da {i}ª pessoa: ').strip().upper()
    idade = int(input(f'Idade: ').strip())
    sexo = input(f'Sexo [M/F]: ').strip().upper()

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    elif sexo == 'F' and idade < 20:
        total_mulheres_menor_20 += 1


print(f'\nA idade média é de {soma_idades / total_pessoas:.1f} anos.')

if len(homem_mais_velho) > 0:
    print(f'O homem mais velho tem {idade_homem_mais_velho} anos e '
          f'se chama {homem_mais_velho}.')
else:
    print('Não tem homens no grupo.')

if total_mulheres_menor_20 > 1:
    print(f'Há {total_mulheres_menor_20} mulheres com menos de 20 anos.')

elif total_mulheres_menor_20 == 1:
    print(f'Há {total_mulheres_menor_20} mulher com menos de 20 anos.')

else:
    print('Não há mulheres com menos de 20 anos.')
