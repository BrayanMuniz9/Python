import os
os.system('cls')

print('Calculo de peso ideal')
altura = float(input('Digite a altura da pessoa em metros: '))
sexo = input('Digite o sexo da pessoa m/f: ')

if sexo in 'mM':
    pesom = (72.7*altura) - 58
    print(f'O peso ideal dessa pessoa é {pesom:.1f}')
elif sexo in 'fF':
    pesof = (62.1*altura) - 44.7
    print(f'O peso ideal dessa pessoa é {pesof:.1f}')
else:
    print(f'Selecione um sexo valido!')