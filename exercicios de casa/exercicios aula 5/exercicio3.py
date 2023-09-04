import os
os.system('cls')

produto = input('Qual o nome do produto: ')
valor = float(input('Qual o valor do produto: R$ '))

if valor < 10.00:
    print(f'O produto {produto} fica no valor de R$ {valor*1.70:.2f}.')
elif valor >= 10.00 or valor < 30.00:
    print(f'O produto {produto} fica no valor de R$ {valor*1.50:.2f}.')
elif valor >= 30.00 or valor < 50.00:
    print(f'O produto {produto} fica no valor de R$ {valor*1.40:.2f}.')
else:
    print(f'O produto {produto} fica no valor de R$ {valor*1.30:.2f}.')
