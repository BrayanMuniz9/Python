import os
os.system('cls')

valorprestacao = float(input('Valor da prestação atrasada R$ '))
multa = float(input('Porcentagem da multa: '))
qntdedia = int(input('Quantidade de dias atrasados: '))

prestacao = valorprestacao+(valorprestacao*(multa/100)*qntdedia)

print(f'O valor da prestação foi ajustado para {prestacao}.')
