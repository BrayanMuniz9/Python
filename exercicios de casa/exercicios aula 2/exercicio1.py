import os
os.system('cls')

largura = float(input('Digite o valor da largura do retangulo: '))
altura = float(input('Digite o valor do altura lado do retangulo: '))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f'A área do retangulo é {area} e o perimetro é {perimetro}.')
