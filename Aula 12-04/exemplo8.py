import os
os.system('cls')

cont = 0
soma = 0

while True:
    num = int(input('Digite um numero inteiro (ou -1 para sair): '))
    if num < 0:
        break
    soma = soma + num
    cont = cont + 1

media = soma/cont
print(f' A media dos numeros digitados é: {media:.2f}')
