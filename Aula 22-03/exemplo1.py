import math, os
os.system('cls')

# and or not (e, ou, não)

idade = int(input('Digite a sua idade: '))

if idade >= 16 and idade < 18 and idade >=65:
    print('Voce pode votar se quiser mas não é obrigatorio.')

else:
    print('Voce tem que votar, é obrigatorio.')
    