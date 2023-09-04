import os
os.system('cls')

bin = input('Digite um numero binario: ')
n = len(bin)-1

dec = 0

for d in bin:
    dec = dec + int(d)*2**n
    n = n - 1

print(dec)
