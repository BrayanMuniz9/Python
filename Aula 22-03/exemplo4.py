import os
os.system('cls')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if c > b and a > b:
    print(f'{a} e {c} é maior que {b}')
else:
    print(f'{b} é menor que {a} e {c}')
    