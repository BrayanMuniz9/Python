import os, math
os.system('cls')

m2 = float(input('Digite a área a ser pintada (em m²): '))

l1 = (m2 / 3) / 18
l2 = math.ceil(l1)
preco = l2 * 80.00

print(f'Voce precisara comprar {math.ceil(l2)} latas\nO valor total a pagar será de R$ {preco:.2f}.')