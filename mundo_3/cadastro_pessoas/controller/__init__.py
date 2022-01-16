def existe_arquivo(nome_arq):
    try:
        arq = open(nome_arq, 'r')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arq):
    arq = open(nome_arq, 'w')
    arq.close()


def obter_registros(nome_arq):
    try:
        arquivo = open(nome_arq, 'r')
        conteudo = arquivo.readlines()

        arquivo.close()

        return conteudo
    except FileNotFoundError:
        return None


def inserir_registros(nome_arq, registros):
    conteudo = []

    if not existe_arquivo(nome_arq):
        criar_arquivo(nome_arq)
    else:
        conteudo = obter_registros(nome_arq)

    conteudo.extend(registros)

    arquivo = open(nome_arq, 'w')
    arquivo.writelines(conteudo)

    arquivo.close()
