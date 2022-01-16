# Exercício 101 - Verificar obrigatoriedade de voto para um pessoa
#
# Programa que define uma função chamada voto() que recebe como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto OBRIGATÓRIO nas eleições.


def voto(ano_nasc):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    situacao = f'Com {idade} anos, '

    if idade < 16:
        situacao += 'você AINDA NÃO VOTA!'
    elif idade < 18 or idade >= 65:
        situacao += 'o voto é OPCIONAL!'
    else:
        situacao += 'o voto é OBRIGATÓRIO!'

    return situacao


ano = int(input('\nEm que ano você nasceu? ').strip())
print(voto(ano))
