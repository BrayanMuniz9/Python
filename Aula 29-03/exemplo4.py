import os
os.system('cls')

print('Calculo de IMC')
peso = float(input(f'Qual o peso da pessoa em kg: '))
altura = float(input(f'Qual a altura da pessoa em m: '))

imc = peso / altura ** 2

if imc < 20:
    print('A pessoa está abaixo do peso!')
elif imc < 25:
    print('A pessoa está com o peso normal!')
elif imc < 30:
    print('A pessoa está com sobrepeso!')
elif imc < 40:
    print('A pessoa está obesa!')
else:
    print('Obeso morbido!')
