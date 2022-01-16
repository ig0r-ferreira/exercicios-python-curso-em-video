# Algoritmo que converte uma temperatura em graus Celsius e
# converte para graus Fahrenheit.

tc = float(input('Digite uma temperatura em °C: ').strip())

tk = ((9 * tc) / 5) + 32

print(f'\nA temperatura de {tc}°C corresponde a {tk}°F.')
