# Exercício 39 - Alistamento Militar
#
# Algoritmo que lê o ano de nascimento de um jovem e informa, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar e quanto tempo falta, se é a hora exata de
# se alistar ou se já passou do tempo do alistamento e quanto tempo passou.


from sys import exit
from datetime import date


def calcdif(d1, d2):
    total_dias = (d2 - d1).days

    dif_dias = (total_dias % 365) % 30
    dif_meses = (total_dias % 365) // 30
    dif_anos = total_dias // 365

    dif = ''

    if dif_anos > 0 and dif_meses > 0:
        dif += str(dif_anos) + (' ano' if dif_anos == 1 else ' anos') + ' e ' + \
               str(dif_meses) + (' mês' if dif_meses == 1 else ' meses')

    elif dif_anos > 0:
        dif += str(dif_anos) + (' ano' if dif_anos == 1 else ' anos')
    elif dif_meses > 0:
        dif += str(dif_meses) + (' mês' if dif_meses == 1 else ' meses')
    else:
        dif += str(dif_dias) + (' dia' if dif_dias == 1 else ' dias')

    return dif


print('\nAlistamento Militar')


nome = input('\nSeu nome: ').strip()

# Verifica se o conteúdo da string é alfabético simulando a substituição de
# todos os espaços em branco por caracteres vazios
if not nome.replace(" ", "").isalpha():
    exit('\nErro: Você não informou um nome!')

# Remove os espaços antes e depois do nome e o coloca em maiúsculo
nome = nome.strip().upper()

sexo = input('Sexo [masculino/feminino]: ').strip().lower()

# Finaliza o programa caso o sexo não seja masculino ou feminino
if not sexo == 'masculino' or sexo == 'feminino':
    exit('\nErro: Você não informou o sexo. Tente novamente!')

if sexo == 'feminino':
    exit('\nO alistamento é obrigatório somente para o sexo masculino!')

ano_nasc = input('Ano de nascimento: ').strip()

data_atual = date.today()

# Se o ano não for númerico ou se for menor que o ano atual menos 130
if not ano_nasc.isnumeric() or int(ano_nasc) < (data_atual.year - 130):
    exit('\nErro: Ano inválido!')

ano_nasc = int(ano_nasc)
idade = data_atual.year - ano_nasc

prazo_inicio = date((ano_nasc + 18), 1, 1)
prazo_fim = date((ano_nasc + 18), 6, 30)


# Se idade for menor que 18 anos, calcula e mostra o tempo que falta para se alistar
if idade < 18:
    tempo_restante = calcdif(data_atual, prazo_inicio)

    print(f'\nCaro {nome}, ainda falta {tempo_restante} para você se alistar!')

# Se a idade for igual a 18 anos e está dentro do prazo, informa a urgência do alistamento
elif idade == 18 and data_atual <= prazo_fim:
    print(f'\nCaro {nome}, já está no período para você se alistar!'
          f'\nVocê deverá se apresentar imediatamente!')

# Se a idade for maior que 18 anos, calcula e mostra quanto tempo passou desde o período do
# alistamento
else:
    tempo_atraso = calcdif(prazo_fim, data_atual)

    print(f'\nCaro {nome}, já passou {tempo_atraso} desde o período do alistamento!'
          f'\nVocê será multado por faltar com suas obrigações para com o país.')
