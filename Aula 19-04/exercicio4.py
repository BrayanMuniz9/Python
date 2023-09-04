import os
os.system('cls')

soma = 0
conta = input('Digite a conta: ')

for n in conta:
    soma += int(n)

digito = soma % 10

print(f'Numero da conta completo: 00{conta}-{digito}')