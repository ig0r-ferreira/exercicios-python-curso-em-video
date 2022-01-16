# Exercício 104 - Validação de entrada de números inteiros
#
# Programa que define uma função ler_int(), que funciona de forma semelhante a função input() do
# Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = ler_int(‘Digite um n: ‘)


def ler_int(texto):
    while True:
        entrada = input(texto).strip()
        if entrada.isnumeric():
            return int(entrada)
        else:
            print('\033[1;31mERRO! Você não digitou um número inteiro!\033[m')


n = ler_int('\nDigite um número: ')
print('\033[1;32mVocê digitou um número inteiro!\033[m')
