# Exercício 115 - Sistema de Cadastro de Pessoas


from cadastro_pessoas.view import *


while True:
    opcao = menu(titulo='MENU PRINCIPAL',
                 opcoes=['Cadastrar pessoa', 'Listar pessoas', 'Limpar dados', 'Sair'])

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        limpar()
    elif opcao == 4:
        mostrar_finalizacao()
        break
    else:
        mostrar_erro('Opção inválida. Por favor, digite 1, 2 ou 3!')
