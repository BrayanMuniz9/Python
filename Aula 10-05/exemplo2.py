import os
os.system('cls')

notas = [6, 7, 6.5, 4.8, 8]

soma = 0
cont = 0
for n in notas:
    soma += n
    media = soma / len(notas)

print(f'A media é {media:.2f}')

for i in range(len(notas)):
    if notas[i] > media:
        cont += 1
print(f'Notas acima da media: {cont}')
