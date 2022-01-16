# Exercício 57 - Validação de dados
#
# Algoritmo que lê o sexo de uma pessoa, aceitando somente os valores 'M' e 'F'. Caso não
# seja informado corretamente ele solicita novamente até que seja digitado um dos valores
# permitidos.


print()

sexo = ''

while sexo != 'M' and sexo != 'F':

    sexo = input('Informe seu sexo [M/F]: ').strip().upper()

    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mErro: Opção inválida. Tente novamente!\033[m')

if sexo == 'M':
    print('\nVocê é do sexo MASCULINO.')
else:
    print('\nVocê é do sexo FEMININO.')
