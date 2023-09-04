import os
os.system('cls')

h = float(input('Altura da piramide: '))
bmenor = float(input('Valor da base menor: '))
bmaior = float(input('Valor da base maior: '))

volume = h / 3 * (bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)

print(f'O volume do tronco da piramide é: {volume}')
