# Algoritmo que lê as duas notas de um aluno, calcula e mostra a média.

nota1 = float(input('Primeira nota do aluno: ').strip())
nota2 = float(input('Segunda nota do aluno: ').strip())

media = (nota1 + nota2) / 2

print(f'\nA média do aluno é {media:.2f}.')
