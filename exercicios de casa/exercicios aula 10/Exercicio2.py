import os
os.system('cls')

num = input('Digite um número inteiro com 3 algarismos: ')
inverso = (num[::-1])
eq = int(num) + int(inverso)
print(f'{num} + {inverso} = {eq}')