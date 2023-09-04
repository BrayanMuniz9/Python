import os
os.system('cls')

n = int(input('Digite um numero inteiro: '))

s = 0

for num in range(1, n+1):
    s += 1 / num

print(f'A soma: {s:.2F}')