import math, os
os.system('cls')

num = float(input('Digite um numero real: '))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.trunc(absoluto))

print(f'De acordo com o numero {num} \nValor absoluto: {absoluto} \nSua parte inteira: {inteiro} \nSua raiz quadrada: {raiz:.2f} \nO fatorial desse numero: {fatorial}')
