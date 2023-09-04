import os
os.system('cls')

nome = input('Digite o seu nome: ')
disciplina = input('Digite sua disciplina: ')
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
media = (nota1+nota2) / 2

print(f'Nome: {nome}')
print(f'Disciplina: {disciplina}')
print(f'Nota 1: {nota1:.2f}')
print(f'Nota 2: {nota2:.2f}')
print(f'Media: {media:.2f}')
