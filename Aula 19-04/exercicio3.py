import os
os.system('cls')

x = 0
soma = 0

for alunos in range(500):
    idade = int(input(f'Digite a idade do {alunos+1}º aluno: '))
    soma += idade

    if idade > 16:
        x += 1
    
media = soma / 10

print(f'A media de idade dos alunos é {media} e a quantidade que pode votar é {x}')
