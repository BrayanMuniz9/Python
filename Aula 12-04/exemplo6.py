resp = "s"
cont = 0
soma = 0

while resp == 's' or resp == 'S':
    num = int(input('Digite um numero inteiro: '))
    soma = soma + num
    cont = cont + 1
    resp = input('Deseja continuar (s/n)?')

media = soma/cont
print(f' A media dos numeros digitados é: {media:.2f}')
