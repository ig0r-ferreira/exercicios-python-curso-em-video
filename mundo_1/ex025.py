# Algoritmo que lê o nome de uma pessoa e diz se ela tem o sobrenome “SILVA”.


nome = input('Digite seu nome completo: ').strip()

print(f'\nVocê possui o sobrenome SILVA? {" Silva " in nome.title()}')
