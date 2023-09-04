import os, math
os.system('cls')

angulo = int(input('Digite o valor de um angulo em graus: '))
rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print(f'Tendo o angulo de {angulo}º graus.\nSeno {sen:.4f}\nCosseno {cos:.4f}\nTangente {tan:.4f}')
