import os
os.system('cls')

num = int(input('Digite um numero inteiro: '))

# if num % 2 == 0:
#     print(f'O numero {num} é par')
# else:
#     print(f'O numero {num} é impar')
resultado = 'par' if num % 2 == 0 else 'impar'
print(f'O {num} é {resultado}')

input('...')
