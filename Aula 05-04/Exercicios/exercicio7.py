import os
os.system('cls')

print('Coordenadas de um ponto P(x,y)')
x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print(f'O ponto P({x:.1f}, {y:.1f}) pertence ao 1º quadrante')
elif x < 0 and y > 0:
    print(f'O ponto P({x:.1f}, {y:.1f}) pertence ao 2º quadrante')
elif x < 0 and y < 0:
    print(f'O ponto P({x:.1f}, {y:.1f}) pertence ao 3º quadrante')
else:
    print(f'O ponto P({x:.1f}, {y:.1f}) pertence ao 4º quadrante')
