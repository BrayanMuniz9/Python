import os
os.system('cls')

print('Calculo de juros')
valor = float(input('Qual o valor da compra: R$ '))
parc = int(input('Vai parcelar em quantas vezes em ate 12 vezes: '))

if valor < 0:
    print('Insira um valor valido!')

if parc < 2:
    print(f'Se for parcelar 1x não tem juros, ainda fica R$ {valor} reais.')
elif parc >= 2 and parc < 4:
    valor1 = valor * 1.03
    print(f'Se for dividir em {parc}x tem 3% de juros, tendo um total de R$ {valor1/parc} reais.')
elif parc >= 4 and parc < 6:
    valor2 = valor * 1.07
    print(f'Se for dividir em {parc}x tem 7% de juros, tendo um total de R$ {valor2/parc} reais.')
elif parc >= 6 and parc < 8:
    valor3 = valor * 1.09
    print(f'Se for dividir em {parc}x tem 9% de juros, tendo um total de R$ {valor3/parc} reais.')
elif parc >= 8 and parc <= 12:
    valor4 = valor * 1.12
    print(f'Se for dividir em {parc}x tem 12% de juros, tendo um total de R$ {valor4/parc} reais.')
else:
    print('Insira um valor de parcelas corretos!')
