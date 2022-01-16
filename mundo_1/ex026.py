# Algoritmo que lê uma frase pelo teclado e mostra quantas vezes aparece a letra “A”,
# em que posição ela aparece pela primeira vez e em que posição ela aparece pela
# última vez.


frase = input('Digite uma frase: ').strip()

print(f'\nTotal de vezes que a letra A aparece: {frase.upper().count("A")}')
print(f'A letra A aparece pela primeira vez na posição {frase.upper().find("A")}.')
print(f'A letra A aparece pela última vez na posição {frase.upper().rfind("A")}.')
