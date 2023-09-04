import os
os.system('cls')

num = int(input('Digite um numero inteiro: '))

if num > 0:
    print(f'O numero {num} é positivo!')
elif num == 0:
    print(f'O numero {num} é nulo')
else:
    print(f'O numero {num} é negativo!')