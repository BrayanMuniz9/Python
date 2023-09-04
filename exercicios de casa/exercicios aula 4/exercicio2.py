import os
os.system('cls')

turno = input('Utilize um caractere para representar\nNOITE (N) \nMANHA (M) \nTARDE (T)\nQual o seu turno de trabalho ?: ')
hora = int(input('Quantas horas voce trabalha em um dia: '))

if turno == 'N' or turno == 'n':
    print(f'O valor do seu dia trabalhado é R${hora * 45.00}.')
else:
    print(f'O valor do seu dia trabalhado é R${hora * 37.50}.')
