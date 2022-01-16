# Exercício 102 - Fatorial utilizando função
#
# Programa que define uma função fatorial() que recebe dois parâmetros: o primeiro indicará o
# o valor a ser calculado e o outro chamado show, será um valor lógico (opcional) que indicará se
# será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    Função que calcula o fatorial do número informado.
    :param num: Número que será utilizado para calcular o fatorial.
    :param show: (Opcional) Mostra o cálculo do fatorial.
    :return: Fatorial de num.
    """
    f = 1

    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')

    if show:
        print(f)

    return f


print(f'\n{" CÁLCULO DO FATORIAL ":=^45}\n')

n = int(input('Digite um número: ').strip())
print(f'O fatorial de {n} é {fatorial(n, show=True)}.')
