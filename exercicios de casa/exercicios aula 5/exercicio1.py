import os
os.system('cls')

idade = int(input('Quantos anos você tem ? '))

print('De acordo com a sua idade.')

if idade >= 16 and idade < 18 or idade > 65:
    print('Voce é um eleitor facultativo')
elif idade >= 18 and idade <= 65:
    print('Voce é eleitor obrigatorio')
else:
    print('Voce ainda não é eleitor')
