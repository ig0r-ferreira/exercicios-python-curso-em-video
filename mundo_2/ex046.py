# Exercício 46 - Contagem regressiva para o Ano Novo
#
# Algoritmo que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# do Ano Novo, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep
from emoji import emojize


print()
print(emojize(":cone_de_festa:", language="pt") * 3, end=' ')
print('Iniciando contagem para o Ano Novo!!!', end=' ')
print(str(emojize(":cone_de_festa:", language="pt") * 3) + '\n')

for i in range(10, -1, -1):
    sleep(1)
    print(f'{i:02}'.center(48))

sleep(1)

msg_final = str(emojize(":fogos_de_artifício:", language="pt") * 9)
msg_final += ' Feliz Ano Novo!!! '
msg_final += str(emojize(":fogos_de_artifício:", language="pt") * 9)

print('\n' + msg_final)
