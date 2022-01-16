# Exercício 94 - Armazenando dados de pessoas utilizando dicionários
#
# Programa que lê o nome, sexo e idade de várias pessoas, e monta um dicionário para cada pessoa em
# seguida armazena todos os dicionários em uma lista. Ao final, é mostrado:
#
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


from numpy import mean


pessoas = []

print(f'\n{" CADASTRAR PESSOA ":=^50}')

while True:
    pessoa = {
        'nome': input('\nNome: ').strip().upper()
    }

    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('ERRO! Digite apenas M ou F.')

    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: ').strip())

    pessoas.append(pessoa)

    print()

    while True:
        continuar = input('=> Deseja continuar [S/N]? ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break

idades = list(map(lambda p: p['idade'], pessoas))
media_idade = mean(idades)

mulheres = [p for p in pessoas if p['sexo'] == "F"]
pessoas_idade_maior_media = [p for p in pessoas if p['idade'] > media_idade]


print(f'\n\n{"":=^50}\n')

print(f'=> Foram cadastradas {len(pessoas)} pessoa(s).')
print(f'=> A média de idade das pessoas cadastradas é de {media_idade:.0f} anos.')
print('=> Mulheres cadastradas: ', end='')
if len(mulheres) > 0:
    print()
    for mulher in mulheres:
        print(f'\t- {mulher["nome"]}, {mulher["idade"]} anos')
else:
    print('Nenhuma')

print(f'=> Pessoas com idade superior a média: ', end='')
if len(pessoas_idade_maior_media) > 0:
    print()
    for pessoa in pessoas_idade_maior_media:
        print(f'\t- {pessoa["nome"]}, {pessoa["idade"]} anos, '
              f'sexo {"masculino" if pessoa["sexo"] == "M" else "feminino"}')
else:
    print('Nenhuma')
