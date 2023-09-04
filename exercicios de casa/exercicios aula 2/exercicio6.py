cliente = input('Qual o nome do cliente: ')
mesa = input('Nº da mesa: ')
gasto = float(input('Quanto foi gasto pelo cliente: R$'))

porcentagem = gasto * (10/100)
valorf = porcentagem + gasto

print(f'O cliente {cliente} da mesa {mesa} gastou no total de R${gasto:.2f} reais, considerando a gorjeta de 10% do garçom o valor total fica R${valorf:.2f} reais.')
