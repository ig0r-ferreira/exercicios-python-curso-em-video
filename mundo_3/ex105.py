# Exercício 105 - Analisando notas
#
# Programa que define uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def analisar_notas(*notas, sit=False):
    """
    Função que analisa as notas informadas e fornece detalhes sobre o desempenho do aluno.
    :param notas: Notas do aluno, parâmetro multivalorado.
    :param sit: (Opcional) Caso verdadeiro mostra a situação do aluno de acordo com sua média.
    :return: Dicionário com detalhes sobre a nota.
    """

    detalhes = {
        'quant_notas': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'media': sum(notas) / len(notas)
    }
    if sit:
        if detalhes['media'] < 3:
            detalhes['situacao'] = 'PÉSSIMA'
        elif detalhes['media'] < 6:
            detalhes['situacao'] = 'RUIM'
        elif detalhes['media'] < 8:
            detalhes['situacao'] = 'REGULAR'
        elif detalhes['media'] < 9:
            detalhes['situacao'] = 'BOA'
        else:
            detalhes['situacao'] = 'EXCELENTE'

    return detalhes


print(analisar_notas(5.5, 2.5, 1.5, sit=True))
