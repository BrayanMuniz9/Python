import os, math
os.system('cls')

r = float(input('Digite o raio de um circulo em cm: '))

area = math.pi * r ** 2
comprimento = 2 * math.pi * r

print(f'Área do circulo: {area:.2f} cm²\nComprimento do circulo: {comprimento:.2f} cm')
