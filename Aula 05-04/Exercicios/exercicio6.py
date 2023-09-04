import os, math
os.system('cls')

n1 = float(input('Digite a primeira nota parcial: '))
n2 = float(input('Digite a segunda nota parcial: '))

m = (n1 + n2) / 2

if n1 > 10 or n2 > 10:
    print('Insira uma nota valida')
elif m <= 10 and m >= 9:
    print('Conceito A\nAprovado!')
elif m <= 8.9 and m >= 7.5:
    print('Conceito B\nAprovado!')
elif m <= 7.4 and m >= 6.0:
    print('Conceito C\nAprovado!')
elif m <= 5.9 and m >= 4.0:
    print('Conceito D\nAprovado!')
else:
    print('Conceito E\nReprovado!')
