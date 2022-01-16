# Exercício 37 - Conversor de bases
#
# Algoritmo que lê um número inteiro qualquer e pede para o usuário escolher qual será
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


num = int(input('Digite um número inteiro: ').strip())

escolha = int(input("""
Escolha a base:
[ 1 ] \033[2;32mBINÁRIO\033[m
[ 2 ] \033[2;31mOCTAL\033[m
[ 3 ] \033[2;34mHEXADECIMAL\033[m

Base: """).strip())

if escolha == 1:
    print(f'\n{num} corresponde a {bin(num)[2:]} em BINÁRIO.')
elif escolha == 2:
    print(f'\n{num} corresponde a {oct(num)[2:]} em OCTAL.')
elif escolha == 3:
    print(f'\n{num} corresponde a {hex(num)[2:]} em HEXADECIMAL.')
else:
    print('\nVocê não escolheu uma base!')
