# Exercício 111 - Testando o uso de pacotes
#
# Programa que testa a utilização do módulo moeda que foi transformado em um pacote e colocado
# dentro de outro pacote chamado utils.


from utils.moeda import resumo

valor = float(input('\nDigite um valor: R$ ').strip())
resumo(valor, aum=25, red=17)
