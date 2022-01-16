# Algoritmo que lê o nome de quatro alunos e mostra a ordem sorteada para apresentação
# de trabalhos.

from random import sample

a1 = input('Primeiro aluno: ').strip()
a2 = input('Segundo aluno: ').strip()
a3 = input('Terceiro aluno: ').strip()
a4 = input('Quarto aluno: ').strip()

alunos = [a1, a2, a3, a4]

print('\nA ordem de apresentação será: ', end='')
print(', '.join(sample(alunos, k=4)))
