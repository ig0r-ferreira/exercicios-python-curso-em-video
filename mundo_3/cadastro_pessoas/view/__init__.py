from time import sleep
from mundo_3.cadastro_pessoas.controller import *


def menu(titulo, opcoes):
    while True:
        mostrar_titulo(titulo, cor='ciano', negrito=True, br_ant=2, br_dep=2)

        for i in range(0, len(opcoes)):
            print(f'{font_color(negrito=True)}[ ' + str(i + 1) + f' ]{font_color("neutro")} - ' +
                  str(opcoes[i]).strip())

        try:
            opcao = int(input(f'\n{font_color(cor="vermelho", negrito=True)}'
                              f'Opção:'
                              f'{font_color("neutro")} ').strip())

            return opcao

        except ValueError:
            mostrar_erro('Opção inválida. Por favor, digite 1, 2 ou 3!')


def mostrar_titulo(titulo, cor='neutro', negrito=False, br_ant=0, br_dep=1):
    print('\n' * br_ant, end='')
    print(f'{font_color(cor, negrito)}'
          f'{f" {titulo} ":=^50}'
          f'{font_color("neutro")}', end='\n' * br_dep)


def mostrar_linha(cor='neutro', negrito=False, br_ant=0, br_dep=1):
    print('\n' * br_ant, end='')
    print(f'{font_color(cor, negrito)}' + '=' * 50 + font_color('neutro'), end='\n' * br_dep)


def mostrar_mensagem(msg, cor='neutro', negrito=False, br_ant=0, br_dep=1):
    print('\n' * br_ant, end='')
    print(f'{font_color(cor, negrito)}'
          f'{msg}'
          f'{font_color("neutro")}', end='\n' * br_dep)


def mostrar_erro(erro):
    print(f'{font_color("vermelho", negrito=True)}'
          f'ERRO: {erro}'
          f'{font_color("neutro")}')


def mostrar_finalizacao():
    mostrar_mensagem('SAINDO DO PROGRAMA...', cor='ciano', negrito=True, br_ant=1)
    sleep(2)


def font_color(cor='neutro', negrito=False):
    negrito = '1' if negrito is True else '0'
    cores = {
        'neutro': f'\033[{negrito}m',
        'branco': f'\033[{negrito};30m',
        'vermelho': f'\033[{negrito};31m',
        'verde': f'\033[{negrito};32m',
        'amarelo': f'\033[{negrito};33m',
        'azul': f'\033[{negrito};34m',
        'violeta': f'\033[{negrito};35m',
        'ciano': f'\033[{negrito};36m',
        'cinza': f'\033[{negrito};37m',
    }
    return cores[cor]


def cadastrar():
    cor_tema = 'verde'
    mostrar_titulo('NOVO CADASTRO', cor_tema, negrito=True, br_ant=2, br_dep=2)

    while True:
        nome = input(f'{font_color(negrito=True)}'
                     f'Nome:'
                     f'{font_color(negrito=True)} ').strip().upper()

        if not nome.replace(' ', '').isalpha():
            mostrar_erro('Nome inválido. Por favor, tente novamente!')
        else:
            break

    while True:
        try:
            idade = int(input(f'{font_color(negrito=True)}'
                              f'Idade:'
                              f'{font_color(negrito=True)} ').strip())
        except ValueError:
            mostrar_erro('Idade inválida. Por favor, tente novamente!')
        else:
            break

    inserir_registros('pessoas.txt', [nome + ';' + str(idade) + '\n'])

    sleep(1)
    mostrar_linha(cor_tema, negrito=True, br_ant=1)
    mostrar_mensagem('=> Pessoa cadastrada com sucesso!', cor=cor_tema, negrito=True)
    sleep(1.5)


def listar():
    cor_tema = 'amarelo'
    mostrar_titulo('PESSOAS CADASTRADAS', cor_tema, negrito=True, br_ant=2, br_dep=2)

    pessoas = obter_registros('pessoas.txt')

    if pessoas:
        for dados in pessoas:
            dados = dados.replace('\n', '').split(';')
            nome = dados[0]
            idade = dados[1]
            print(f'=> {font_color(negrito=True) + nome + font_color("neutro"):<46}' +
                  f'{idade:>3} anos')
    else:
        mostrar_mensagem('VAZIO', negrito=True)

    mostrar_linha(cor_tema, negrito=True, br_ant=1)
    sleep(1.5)


def limpar():
    cor_tema = 'neutro'

    dados = obter_registros('pessoas.txt')

    if dados:
        listar()
        print()

        while True:
            continuar = input(f'{font_color("vermelho", negrito=True)}'
                              f'Você deseja continuar com a exclusão dos dados [S/N]?'
                              f'{font_color("neutro")} ').strip().upper()
            if continuar == 'S' or continuar == 'N':
                break

        mostrar_linha(cor=cor_tema, negrito=True, br_ant=1)

        if continuar == 'S':
            criar_arquivo('pessoas.txt')
            mostrar_mensagem('=> Dados excluídos com sucesso!', cor=cor_tema, negrito=True)
        else:
            mostrar_mensagem('=> Operação cancelada!', cor=cor_tema, negrito=True)
    else:
        mostrar_linha(cor=cor_tema, negrito=True, br_ant=1)
        mostrar_mensagem('=> Não há dados para serem deletados!', cor=cor_tema, negrito=True)
