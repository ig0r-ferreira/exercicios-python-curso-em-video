# Exercício 90 - Dicionário em Python
#
# Programa que lê o nome e média de um aluno, guardando também a situação em um dicionário.
# Ao final, mostra o conteúdo da estrutura na tela.


print(f'\n{" SITUAÇÃO DO ALUNO ":=^51}\n')

aluno = {'nome': input('Nome do aluno: ').strip()}

while True:
    aluno['media'] = float(input('Média: ').strip())
    if 10 >= aluno['media'] >= 0:
        break
    else:
        print('* Media inválida! Informe um valor de 0 a 10.')

if aluno['media'] >= 7:
    aluno['situacao'] = '\033[1;32mAPROVADO\033[m'
elif aluno['media'] >= 5:
    aluno['situacao'] = '\033[1;33mEM RECUPERAÇÃO\033[m'
else:
    aluno['situacao'] = '\033[1;31mREPROVADO\033[m'

print(f'\n{aluno["nome"]} teve média {aluno["media"]:.1f}, portanto está {aluno["situacao"]}!')
