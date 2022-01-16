# Exercício 77 - Contando vogais em Tuplas
#
# Programa que tem uma tupla com várias palavras (não usar acentos).
# E para cada palavra, ele mostra quais são as suas vogais.


palavras = ('Programar', 'Py', 'Curso', 'Estudar', 'Conhecimento')

print(f'\n{" CONTAGEM DE VOGAIS ":=^50}\n')

for p in palavras:

    print(f'{f"{p.upper()} ":-<30} Vogais: ', end='')

    cont = 0

    if 'a' in p:
        print('a', end=' ')
    else:
        cont += 1
    if 'e' in p:
        print('e', end=' ')
    else:
        cont += 1
    if 'i' in p:
        print('i', end=' ')
    else:
        cont += 1
    if 'o' in p:
        print('o', end=' ')
    else:
        cont += 1
    if 'u' in p:
        print('u', end=' ')
    else:
        cont += 1
    if cont == 5:
        print('Nenhuma', end=' ')
    print()
