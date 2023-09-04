import os
os.system('cls')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'O primeiro numero {n1} é o maior')
elif n2 > n1 and n2 > n3:
    print(f'O segundo numero {n2} é o maior')
else:
    print(f'O terceiro numero {n3} é o maior')
