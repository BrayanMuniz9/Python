import os
os.system('cls')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

medianota = (nota1 + nota2) / 2

if medianota >= 6.0:
    print(f'Parabens voce passou de ano, sua media é {medianota:.1f}.')
else:
    print(f'Se fodeu otario repetiu de ano, sua media é {medianota:.1f}.')