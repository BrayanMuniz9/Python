import os, math
os.system('cls')

turma = int(input('Digite a quantidade de turmas: '))
cont = 0
for x in range(turma):
    alunos = int(input(f'Digite a quantidade de alunos da {x+1}ª turma: '))
    cont += alunos

media = cont / turma

print(f'As turmas tem em media {math.ceil(media)} alunos.')
