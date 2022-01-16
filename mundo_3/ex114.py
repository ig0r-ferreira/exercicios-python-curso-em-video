# Exercício 114 - Fazendo uma requisição para um site


import requests


url = 'http://pudim.com.br'

try:
    req = requests.get(url)

    if req.status_code == 200:
        print('\n\033[1;32mConsegui acessar o site pudim.com.br com sucesso!\033[m')
    else:
        print('\n\033[1;31mNão foi possível acessar o site pudim.com.br!\033[m')

except requests.exceptions.ConnectionError:
    print('\n\033[1;31mNão foi possível acessar o site pudim.com.br!\033[m')
