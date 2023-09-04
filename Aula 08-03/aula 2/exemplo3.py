import os
os.system('cls')

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
restodivisao = num1 % num2
 
print(f'A soma de {num1} com {num2} é = {soma}')
print(f'A Subtração de {num1} com {num2} é = {subtracao}')
print(f'A multiplicação de {num1} com {num2} é = {multiplicacao}')
print(f'O {num1} divido por {num2} é = {divisao}')
print(f'O resto da divisão entre {num1} e {num2} é = {restodivisao}')
