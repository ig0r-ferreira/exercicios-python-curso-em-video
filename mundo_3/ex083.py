# Exercício 83 - Validando expressões matématicas
#
# Programa no qual o usuário poderá digitar uma expressão qualquer que use parênteses e indicará se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.


exp_mat = input('\nDigite uma expressão matemática (com parênteses): ').strip()

total_abertos = exp_mat.count('(')
total_fechados = exp_mat.count(')')

if total_abertos == total_fechados:
    print('\nExpressão válida.')
elif total_abertos > total_fechados:
    print(f'\nExpressão inválida! Você esqueceu de fechar '
          f'{total_abertos - total_fechados} parêntese(s).')
else:
    print(f'\nExpressão inválida! Você esqueceu de abrir '
          f'{total_fechados - total_abertos} parêntese(s).')
