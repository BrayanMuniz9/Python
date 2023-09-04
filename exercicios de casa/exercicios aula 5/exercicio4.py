import os
os.system('cls')

print("Calculadora")

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

sinal = input('Selecione o sinal da operação que deverá ser feita;\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/)\n')

if sinal in '+':
    print(f'O resultado da soma de {num1} + {num2} = {num1+num2}')
elif sinal in '-':
    print(f'O resultado da soma de {num1} - {num2} = {num1-num2}')
elif sinal in '*':
    print(f'O resultado da soma de {num1} * {num2} = {num1*num2}')
elif sinal in '/':
    print(f'O resultado da soma de {num1} / {num2} = {num1/num2}')
else:
    print(f'Sinal de operação invalido!')
