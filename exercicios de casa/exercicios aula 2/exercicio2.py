import os
os.system('cls')

nome = input('Qual o nome do funcionario: ')
salario = float(input('Digite o salario sem acrescimos: '))
comissao = float(input('Porcentagem de comissão: '))

acrescimo = (comissao / 100) * salario
salario2 = salario + acrescimo

print(f'O funcionario {nome} ganhou R$ {acrescimo} reais de comissão, e o salario dele de R${salario} reais, foi ajustado para R$ {salario2} reais.')
