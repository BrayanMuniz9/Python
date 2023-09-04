cont = 0

# for alunos in range(10):
while cont < 3:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input(f'Qual a 1ª nota do {nome}: '))
    nota2 = float(input(f'Qual a 2ª nota do {nome}: '))
    media = (nota1 + nota2) / 2
    print(f'A media do aluno {nome} é {media:.2f}')

    cont = cont + 1
