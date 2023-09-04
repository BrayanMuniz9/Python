import os
os.system('cls')

mb = int(input('Digite o tamanho do arquivo (MB): '))
velo = int(input('Digite a velocidade do link de internet (Mbps): '))

mbtis = mb*8
tempo = mbtis / velo

hora = tempo // 3600
minutos = tempo % 3600 // 60
segundos = tempo % 60

print(f'Tempo aproximado de download ({hora} horas(s), {minutos} minuto(s) e {segundos} segundos(s))')

