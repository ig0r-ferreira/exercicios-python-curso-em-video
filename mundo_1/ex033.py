# Algoritmo que lê três números e mostra qual é o maior e qual é o menor.


num1 = int(input('Primeiro número: ').strip())
num2 = int(input('Segundo número: ').strip())
num3 = int(input('Terceiro número: ').strip())

print(f'\n{max(num1, num2, num3)} é o maior número.')
print(f'\n{min(num1, num2, num3)} é o menor número.')
