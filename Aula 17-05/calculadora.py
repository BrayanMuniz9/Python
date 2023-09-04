import os

menu = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Sair']
soma = lambda a,b: a+b
subt = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b

while True:
    os.system('cls')
    print('Calculadora lambda')
    for n, item in enumerate(menu):
        print(f'[{n+1}]- {item}')
    op = int(input('Digite uma opção: '))
    if op == 5: break
    else:
        n1 = float(input('Digite o 1º numero: '))
        n2 = float(input('Digite o 2º numero: '))
        if op == 1: print(f'{n1} + {n2} = {soma(n1, n2)}')
        elif op == 2: print(f'{n1} - {n2} = {subt(n1, n2)}')
        elif op == 3: print(f'{n1} * {n2} = {mult(n1, n2)}')
        elif op == 4: print(f'{n1} / {n2} = {div(n1, n2)}')
        else: print('Selecione uma opção correta. ')
    input('\nEnter continua...')