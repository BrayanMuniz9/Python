soma = 0

for i in range(10):
    num = float(input(f'Digite o {1+i}º numero: '))
    # soma = soma + num
    soma += num

print(f'A soma dos numeros é {soma}')