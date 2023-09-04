import os, math
os.system('cls')

print('Equação de segundo grau.')

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

delta = (b**2) - 4 * a * c
if a == 0:
    print('Não é equação do segundo grau')
elif delta >= 0:
    x1 = (- b + (math.sqrt(delta))) / (2 * a)
    x2 = (- b - (math.sqrt(delta))) / (2 * a)
    print(f'Tendo como base os valores de A, B e C, o valor de delta é {delta} logo, x1: {x1:.2f} e x2: {x2:.2f}')
else:
    print('Não há raízes reais')