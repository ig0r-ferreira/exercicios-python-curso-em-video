# Exercício 112 - Entrada de dados monetários
#
# Programa que lê um valor a partir de uma função chamada ler_dinheiro() que realiza uma validação de
# dados para aceitar apenas valores que seja monetários. Essa função está contida no módulo dado
# dentro do pacote utils que foi criado no último exercício.


from utils.dado import ler_dinheiro
import utils.moeda as moeda

valor = ler_dinheiro('\nDigite um valor: R$ ')
moeda.resumo(valor, 22, 37)
