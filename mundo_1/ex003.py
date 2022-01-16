valor1 = input('Digite um valor: ').strip()

if valor1.isdecimal():
    valor2 = input('Digite outro valor: ').strip()

    if valor2.isdecimal():
        soma = int(valor1) + int(valor2)

        print(f'\nA soma entre {valor1} e {valor2} é {soma}!')

    else:
        print('\nSegundo valor inválido!')
else:
    print('\nPrimeiro valor inválido!')
