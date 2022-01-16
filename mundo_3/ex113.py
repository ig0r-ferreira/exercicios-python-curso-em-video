# Exercício 113 - Funções com tratamentos de erros
#
# Programa que reescreve a função ler_int() criada no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Além disso, agora conta com uma função adicional
# ler_float() com a mesma funcionalidade.


def ler_int(texto):
    while True:
        try:
            num = int(input(texto).strip())
            return num
        except ValueError:
            print('\033[1;31mERRO: Informe um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número!\033[m')
            return '\033[1;37mnenhum\033[m'


def ler_float(texto):
    while True:
        try:
            num = float(input(texto).strip())
            return num
        except ValueError:
            print('\033[1;31mERRO: Informe um número real!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número!\033[m')
            return '\033[1;37mnenhum\033[m'


num_int = ler_int('Digite um número inteiro: ')
num_real = ler_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {num_int} e o real foi {num_real}.')
