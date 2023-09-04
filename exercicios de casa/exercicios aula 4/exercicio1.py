import os
os.system('cls')

num1 = int(input('Digite um numero que está entre ou igual a 0 e 9: '))

if num1 >= 0 and num1 <= 9:
    print(f'O {num1} é um valor correto.')
else:
    print(f'O {num1} é um valor incorreto.')
