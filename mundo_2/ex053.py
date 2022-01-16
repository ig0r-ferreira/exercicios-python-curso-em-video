# Exercício 53 - Detector de palíndromo
#
# Algoritmo que lê uma palavra ou frase e indica se ela é um palíndromo, desconsiderando
# os espaços.
#
# Obs: Palíndromo é uma palavra, frase ou número que pode ser lido de trás para frente.


print(f'\n{" Detector de Palíndromo ":-^100}')

texto = input('\nDigite uma palavra ou frase: ').strip()

texto = texto.lower().replace(' ', '')
texto_invertido = texto[::-1]

print(f'É um palíndromo? {"Sim" if texto == texto_invertido  else "Não"}')
