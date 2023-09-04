import os
os.system('cls')

notas = [6, 7, 6.5, 4.8, 8]
nomes = ['Ana', 'Marco', 'Gilberto', 'Arthur', 'Kamylla']

soma = 0
cont = 0
for n in notas:
    soma += n
    media = soma / len(notas)

print(f'A media é {media:.2f}')

for i in range(len(notas)):
    if notas[i] > media:
        print(f'{nomes[i]}')        
