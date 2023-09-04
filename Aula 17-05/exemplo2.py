def soma(a, b):
    return a+b

while True:
    n1 = int(input('Qual o primeiro numero: '))
    n2 = int(input('Qual o segundo numero: '))

    print(soma(n1, n2))
    if(input('Deseja continuar ')) in 'nN': break
