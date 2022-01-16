# Exercício 69 - Cadastro de pessoas e resumo das informações coletadas
#
# Programa que lê a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# pergunta se o usuário quer ou não continuar. Ao final, é mostrado:
#
#   A) Quantas pessoas tem mais de 18 anos.
#
#   B) Quantos homens foram cadastrados.
#
#   C) Quantas mulheres tem menos de 20 anos.


continuar = None
total_pessoas = total_maiores18 = total_homens = total_mulheres_menos_20 = 0


while continuar != 'N':
    print(f'\n{" NOVO CADASTRO ":-^50}')
    nome = input('\nNome completo: ').strip().upper()
    idade = int(input('Idade: ').strip())

    sexo = None
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()

    if idade >= 18:
        total_maiores18 += 1

    if sexo == 'M':
        total_homens += 1
    elif idade < 20:
        total_mulheres_menos_20 += 1

    total_pessoas += 1

    print()

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()


print('\nForam cadastradas:\n')
print(f'{total_pessoas} pessoa(s) ao todo, sendo que\n')

if total_maiores18 > 0:
    print(f'Temos {total_maiores18} pessoa(s) com mais de 18 anos.')
else:
    print('Não há pessoas com mais de 18 anos.')

if total_homens > 1:
    print(f'Temos {total_homens} homens.')
elif total_homens == 1:
    print('Temos 1 homem.')
else:
    print('Não há homens.')

if total_mulheres_menos_20 > 0:
    print(f'Temos {total_mulheres_menos_20} mulher(es) com menos de 20 anos.')
else:
    print('Não há mulheres com menos de 20 anos.')
