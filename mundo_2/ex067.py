# Exercício 67 - Tabuada v3.0
#
# Algoritmo que mostra a tabuada para cada valor digitado pelo usuário.
# A execução será interrompida quando o número solicitado for negativo.


while True:
    num = int(input('\nVocê quer a tabuada de qual número? [negativo para sair]: ').strip())
    if num < 0:
        break

    print(f'\n{f" Tabuada de {num} ":-^50}')

    tamanho_result = str(len(str(num * 10)))

    for i in range(0, 11):
        result = num * i
        print(f'{f"{num} x {i:2} = {result:{tamanho_result}}":^50}')

    print('-' * 50)
