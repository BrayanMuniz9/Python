import os
os.system('cls')

cont = 0
soma = 0

while True:
    num = int(input('Digite um numero inteiro: '))
    soma = soma + num
    cont = cont + 1
    resp = input('Deseja continuar (s/n)? ')
    if resp in 'nN':
        break

media = soma/cont
print(f' A media dos numeros digitados é: {media:.2f}')
