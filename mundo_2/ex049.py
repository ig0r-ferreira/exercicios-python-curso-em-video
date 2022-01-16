# Exercício 49 - Tabuada v2.0
#
# Algoritmo que mostra a tabuada de um número que o usuário escolher só que dessa vez
# utilizando a estrutura de repetição: for.


num = int(input('\nVocê quer a tabuada de qual número? ').strip())

print(f'\n{" Tabuada de "+str(num)+" ":-^50}')

for i in range(0, 11):
    print(f'{num} x {i:2} = {num * i}')
