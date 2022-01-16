def ler_dinheiro(texto):
    while True:
        valor = input(texto).strip().replace(',', '.')

        if valor.replace('.', '').isdecimal():
            return float(valor)

        print(f'\033[1;31mERRO: "{valor}" não é um parâmetro válido!\033[m')
