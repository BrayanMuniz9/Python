import os
os.system('cls')
nomes = []

for i in range(5):
    nome = input(f'[{i+1}] Qual o nome da pessoa? ')
    nomes.append(nome)

print(10*'-')

n = int(input('Quem voce quer exibir digite um numero?' ))

print(nomes[n+1])