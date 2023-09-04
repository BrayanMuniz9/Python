import os
os.system('cls')

nome = input('Qual seu nome? ')
hr = float(input('Que horas são (0-23)? '))

if hr < 0 or hr > 23:
    print('Digite uma hora valida!')
elif hr > 5 and hr < 12:
    print(f'Bom dia {nome}')
elif hr > 13 and hr < 18:
    print(f'Boa tarde {nome}')
else:
    print(f'Boa noite {nome}')