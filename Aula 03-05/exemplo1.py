valor = float(input('Digite o valor do produto: R$'))

acr = valor * 1.05
acr = f'R${acr:.2f}' .replace('.',',')

print(f'O valor final com o acrescimo de 5% é {acr}.')