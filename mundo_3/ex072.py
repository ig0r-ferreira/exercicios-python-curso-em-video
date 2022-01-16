# Exercício 72 - Número por extenso
#
# Programa que lê um número pelo teclado (entre 0 e 20) e mostra por extenso, fazendo uso de
# uma tupla para armazenar os valores por extenso.


numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')


print(f'\n{" MOSTRAR NÚMERO POR EXTENSO ":=^80}\n')

while True:
    num = int(input('\nDigite um número entre 0 e 20: ').strip())

    if 0 <= num <= 20:
        print(f'\nVocê digitou o número {numeros[num]}.\n')

        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = input('Você deseja continuar [S/N]? ').strip().upper()

        if continuar == 'N':
            break
    else:
        print('\nErro: Número inválido! Tente novamente.')
