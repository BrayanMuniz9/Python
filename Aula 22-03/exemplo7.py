import os
os.system('cls')

idade = int(input('Digite a suas idade: '))

# Operador ternario
resultado = 'pode' if idade >= 18 else 'não pode'

print(f'Voce {resultado} ter CNH')