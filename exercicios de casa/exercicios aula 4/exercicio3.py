import os
os.system('cls')

print('Calculo de desconto!')
valor = float(input('Informe o valor da compra: R$ '))

if valor > 200.00:
    desconto = valor - (valor * 0.20)
    print(f'A compra no valor de {valor} tem 20% de desconto, ficando um total R$ {desconto} reais')
else:
    print(f'A compra no valor de {valor} não tem desconto!')
