nome = input('Digite seu nome: ').strip()

if nome.isalpha():
    print(f'\nÉ um prazer te conhecer, {nome}!')
elif not nome:
    print('\nÉ necessário informar um nome.')
else:
    print('\nNome inválido.')
