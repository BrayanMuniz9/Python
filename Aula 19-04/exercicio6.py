import os
os.system('cls')

valor_hora = float(input('Digite o valor da hora aula: R$ '))
carga_hr_semanal = int(input('Digite a carga horaria semanal: '))

salario_base = valor_hora * carga_hr_semanal * 4.5
adicional = salario_base * 1/6
salario_final = salario_base + adicional

print(f'Salario final R${salario_final:.2f}')
