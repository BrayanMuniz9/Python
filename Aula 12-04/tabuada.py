import os
os.system('cls')

num = int(input('Digite um numero que deseja fazer a tabuada: '))

for n in range(11):
    print(f'{num} * {n} = {num*n}')
