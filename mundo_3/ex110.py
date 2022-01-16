# Exercício 110 - Função resumo() do módulo moeda
#
# Programa que testa a chamada de um nova função chamada resumo(), que mostra na tela algumas
# informações geradas pelas demais funções do módulo moeda.


from moeda import resumo

valor = float(input('\nDigite um valor: R$ ').strip())
resumo(valor, aum=25, red=17)
