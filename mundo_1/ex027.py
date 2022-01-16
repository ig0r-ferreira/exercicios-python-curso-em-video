# Algoritmo que lê o nome completo de uma pessoa e em seguida mostra o primeiro e o
# último nome separadamente.


nome = input('Digite um nome completo: ').strip()

partes_nome = nome.split()

print(f'\nPrimeiro nome: {partes_nome[0]}')
print(f'Último nome: {partes_nome[len(partes_nome) - 1]}')
