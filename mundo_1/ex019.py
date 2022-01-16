# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um algoritmo que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.

from random import choice

a1 = input('Primeiro aluno: ').strip()
a2 = input('Segundo aluno: ').strip()
a3 = input('Terceiro aluno: ').strip()
a4 = input('Quarto aluno: ').strip()

alunos = [a1, a2, a3, a4]

print(f'\n{choice(alunos)} foi escolhido para apagar o quadro.')
