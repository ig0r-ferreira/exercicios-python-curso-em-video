def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')


def dobro(valor, fmtd=False):
    valor = valor * 2
    return valor if fmtd is False else formatar(valor)


def metade(valor, fmtd=False):
    valor = valor / 2
    return valor if fmtd is False else formatar(valor)


def aumentar(valor, taxa, fmtd=False):
    valor = valor * (1 + (taxa / 100))
    return valor if fmtd is False else formatar(valor)


def diminuir(valor, taxa, fmtd=False):
    valor = valor * (1 - (taxa / 100))
    return valor if fmtd is False else formatar(valor)


def resumo(valor, aum=0, red=0):
    print(f'\n{" RESUMO DO VALOR ":=^50}\n')
    print(f'Valor analisado: {formatar(valor)}')
    print(f'Dobro: {dobro(valor, fmtd=True)}.')
    print(f'Metade: {metade(valor, fmtd=True)}.')
    print(f'Aumento de {aum}%: {aumentar(valor, aum, fmtd=True)}.')
    print(f'Redução de {red}%: {diminuir(valor, red, fmtd=True)}.')
