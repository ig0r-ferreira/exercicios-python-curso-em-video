# Algoritmo que lê um ano qualquer e mostre se ele é bissexto.


ano = int(input('\nDigite um ano para verificar se ele é bissexto: ').strip())

div_quatro = ano % 4 == 0
div_cem = ano % 100 == 0
div_quatrocentos = ano % 400 == 0

bissexto = (div_quatro and not div_cem) or \
           (div_quatro and div_cem and div_quatrocentos)


if bissexto:
    print(f'\n{ano} é um ano bissexto.')
else:
    print(f'\n{ano} NÃO é um ano bissexto.')
