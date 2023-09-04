import os
os.system('cls')

freq = float(input('Qual a frequencia do aluno? '))
nota = float(input('Qual a media do aluno? '))

if freq < 75:
    print('Reprovado por falta! 🤣')
elif nota < 6:
    print('Reprovado por nota! 💕')
else:
    print('Aprovado! 😍')
    