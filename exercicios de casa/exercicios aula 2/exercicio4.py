import os
os.system('cls')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta1 = (b**2)-4*a*c
raiz = delta1 ** (1/2)
x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

print(f'Tendo como base os valores de A, B e C, o valor de delta é {delta1} logo, x1: {x1:.2f} e x2: {x2:.2f}')
