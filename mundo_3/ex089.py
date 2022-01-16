# Exercício 89:
#
# Programa que lê o nome e duas notas de vários alunos e guarda tudo em uma lista composta.
# Ao final, é mostrado um boletim contendo a média de cada um além de permitir que o usuário possa
# mostrar as notas de cada aluno individualmente.


from time import sleep

boletim = []

while True:
    nome = input('\nNome do aluno: ').strip().upper()
    notas = [float(input('Nota 1: ').strip()), float(input('Nota 2: ').strip())]

    aluno = [nome, notas]
    boletim.append(aluno)

    print()

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break


print(f'\n\n{" BOLETIM GERAL DA TURMA ":-^60}\n')
print(f'{"Id":^5}\t\t{"Aluno":35}\t\t{"Média":5}')

for i, aluno in enumerate(boletim):
    nome_aluno = aluno[0]
    media_aluno = (aluno[1][0] + aluno[1][1]) / 2

    print(f'{(i + 1):^5}\t\t{nome_aluno:35}\t\t{media_aluno:.2f}')


while True:
    id_aluno = int(input('\nVocê gostaria de ver a nota de qual aluno? [0 para SAIR] : ').strip())

    if id_aluno == 0:
        break

    id_aluno -= 1

    print()

    if 0 <= id_aluno < len(boletim):
        print(f'=> Notas de {boletim[id_aluno][0]}: {boletim[id_aluno][1]}')
    else:
        print('* Opção inválida! Verifique o boletim e tente novamente.')

print(f'\nFINALIZANDO...')
sleep(1.5)
