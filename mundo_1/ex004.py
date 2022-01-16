texto = input('Digite algo: ').strip()

print(f'\nO tipo primitivo dessa variável é {type(texto)}.')

print(f'\nSó tem espaços? {texto.isspace()}')

print(f'É um número? {texto.isnumeric()}')

print(f'É alfabético? {texto.isalpha()}')

print(f'É alfanumérico? {texto.isalnum()}')

print(f'Está em maiúsculo? {texto.isupper()}')

print(f'Está em minúsculo? {texto.islower()}')

print(f'Está capitalizada? {texto.istitle()}')
