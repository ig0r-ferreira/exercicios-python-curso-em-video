# Exercício 92 - Cadastrando um trabalhador
#
# Programa que lê o nome, ano de nascimento e o número da carteira de trabalho e cadastra-o
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário recebe
# também o ano de contratação e o salário.
#
# Além da idade, é calculado com quantos anos a pessoa vai se aposentar e ao final são mostradas
# todas as informações do trabalhador.


from sys import exit
from datetime import date


print(f'\n{" CADASTRAR TRABALHADOR ":=^50}\n')


trabalhador = {
    'nome': input('Nome completo: ').strip().upper()
}

ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: ').strip())


if ano_nasc >= ano_atual:
    exit('\nErro: Ano inválido!')
if (ano_atual - ano_nasc) < 18:
    exit('\nErro: Você ainda não é maior de idade!')


trabalhador['idade'] = ano_atual - ano_nasc

num_ctps = input('Número da CTPS [0 se não tem]: ')
trabalhador['num_ctps'] = num_ctps.strip() if type(num_ctps) == str else None

if trabalhador['num_ctps'] != '0':
    ano_admissao = int(input('Ano da admissão: ').strip())

    if ano_admissao < (ano_nasc + 18) or ano_admissao > ano_atual:
        print('\nData de contratação inválida!')
        exit(0)

    trabalhador['ano_admissao'] = ano_admissao
    trabalhador['tempo_restante_aposentadoria'] = 35 - (ano_atual - trabalhador['ano_admissao'])
    trabalhador['salario'] = float(input('Salário: R$ ').strip())
else:
    trabalhador['num_ctps'] = None


print(f'\n{" DADOS DO TRABALHADOR ":=^50}\n')

for k, v in trabalhador.items():
    print(f'{k.upper()}: {v}')
