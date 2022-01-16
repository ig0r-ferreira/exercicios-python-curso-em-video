# Algoritmo que lê um valor em metros e o exibe convertido em outras medidas de comprimento.

medida = float(input('Digite um valor (em metros): ').strip())

print(f'\n{medida}m corresponte a:')

km = (medida / 1000)
hm = (medida / 100)
dam = (medida / 10)
dm = (medida * 10)
cm = (medida * 100)
mm = (medida * 1000)

print(f'{km}km, {hm}hm , {dam}dam, {dm:.0f}dm, {cm:.0f}cm, {mm:.0f}mm')
