import os, math
os.system('cls')

sombra = float(input('Qual é o comprimento da sombra em M: '))
ang = float(input('Digite o angulo em graus: '))
ang = math.radians(ang)

altura = math.tan(ang) * sombra
print(f'A altura do predio é {altura:.2f} m')
