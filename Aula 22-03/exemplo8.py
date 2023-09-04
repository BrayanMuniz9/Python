import os
os.system('cls')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

medianota = (nota1 + nota2) / 2

resultado = 'Você passou' if medianota >= 6.0 else 'Você não passou'
print(f'{resultado} na materia, com uma media de {medianota:.2f}.')