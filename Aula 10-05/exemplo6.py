import os
os.system('cls')

nomes = []
notas = []

while True:
    nome = input('Qual o nome do aluno? ')
    n1 = float(input(f'Qual a 1º nota do {nome}: '))
    n2 = float(input(f'Qual a 2º nota do {nome}: '))
    media = (n1+n2)/2
    notas.append(media)
    nomes.append(nome)

    resp = input('Deseja continuar? S/N ').upper()
    if resp == 'N': break
print(10*'-')
for i , e in enumerate(nomes):
    print(f'[{i}]- {e}' )
print(10*'-')

while True:
    i = int(input('Qual o aluno voce deseja consultar? '))
    if notas[i] > 6:
        print(f'O aluno {nomes[i]} foi aprovado')
    else:
        print(f'O aluno {nomes[i]} foi reprovado')
    print(f'Media: {notas[i]:.2f}')
    print(10*'-')
    resp2 = (input('Deseja consultar mais algum aluno? s/n ')).upper()
    if resp2 == 'N': break
    for i , e in enumerate(nomes):
        print(f'[{i}]- {e}' )
    print(10*'-')