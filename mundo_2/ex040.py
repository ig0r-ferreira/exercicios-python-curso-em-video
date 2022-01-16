# Exercício 40 - Média do aluno
#
# Algoritmo que lê duas notas de um aluno e calcula sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO


from sys import exit

aluno = input('\nNome do aluno: ').strip()

if not aluno.replace(' ', '').isalpha():
    exit('\nErro: Você não informou um nome!')

aluno = aluno.strip().upper()

try:
    nota1 = float(input('\nPrimeira nota: ').strip())
    nota2 = float(input('Segunda nota: ').strip())

    media = (nota1 + nota2) / 2

    if media < 5.0:
        print(f'\n{aluno} foi \033[1;31mREPROVADO\033[m!')
    elif media < 7.0:
        print(f'\n{aluno} vai para \033[1;33mRECUPERAÇÃO\033[m!')
    else:
        print(f'\n{aluno} foi \033[1;32mAPROVADO!\033[m')

except ValueError:
    exit('\nErro: Você não informou um valor válido!')
