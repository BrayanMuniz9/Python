import os
os.system('cls')
print('Calculo de comissão')

func = input('Nome do funcionario: ')
salario = float(input('Digite o salario fixo: R$ '))
vendas = float(input(f'Digite o valor das vendas: R$ '))

comissao = vendas * 0.04
total = comissao + salario

print(f'Comissão: R$ {comissao:.2f}\nSalario final: R$ {total:.2f}')
