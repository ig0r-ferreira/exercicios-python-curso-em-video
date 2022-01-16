# Algoritmo que lê o nome de uma cidade e diz se ela começa ou não com o nome “SANTO”.


cidade = input('Digite o nome de uma cidade: ').strip()

print(f'\n{cidade} começa com SANTO? {cidade.upper().startswith("SANTO")}')
