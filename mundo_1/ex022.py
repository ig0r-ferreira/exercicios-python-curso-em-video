# Algoritmo que lê o nome completo de uma pessoa e mostra:
#
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.


import sys

nome = input('Digite um nome completo: ').strip()

# Verifica se o conteúdo da string é alfabético simulando a substituição de
# todos os espaços em branco por caracteres vazios
if not nome.replace(" ", "").isalpha():
    sys.exit('\nErro: Você não informou um nome!')

# Remove os espaços vazios antes e depois do nome
nome = nome.strip()

# Verifica se o total de partes em que o nome foi quebrado é menor que 2
if len(nome.split()) < 2:
    sys.exit('\nErro: Você não informou um nome completo!')

# Preposições comuns em nomes
preposicoes = ['da', 'das', 'de', 'do', 'dos']
nome_formatado = ''

# Para cada preposição
for p in preposicoes:
    # Verifica se o nome contém a preposição e a remove
    if p in nome:
        nome_formatado = nome.replace(p + " ", "")

# Caso o nome contenha preposições verifica se o nome formatado é capitalizado,
# caso contrário verifica se o nome original é capitalizado
if (len(nome_formatado) > 0 and nome_formatado.istitle()) or nome.istitle():
    print(f'\nNome em maiúsculo: {nome.upper()}')
    print(f'Nome em minúsculo: {nome.lower()}')
    print(f'Total de letras: {len(nome.replace(" ", ""))}')
    print(f'Tolal de letras do primeiro nome: {len(nome.split()[0])}')
else:
    print('\nVocê não informou um nome completo!')
