import os
os.system('cls')

print('Pousada do Paulo')
print('S - Simples\nD - Dupla\nT - Triplo')

quarto = input('Qual seria o quarto escolhido? ')
diarias = int(input('Quantos dias voce vai ficar? '))

# if quarto == 'S' or quarto == 's':
if quarto in 'Ss':
    print(f'Sua estadia no quarto simples por {diarias} dias, fica no total de R$ {diarias * 255.50} reais.')
elif quarto == 'D' or quarto == 'd':
    print(f'Sua estadia no quarto duplo por {diarias} dias, fica no total de R$ {diarias * 305.50} reais.')
elif quarto == 'T' or quarto == 't':
    print(f'Sua estadia no quarto triplo por {diarias} fica no total de R$ {diarias * 360.50} reais.')
else:
    print(f'Insira um quarto valido!')
