import os
os.system ('cls')

seg = int(input('Digite a quantidade segundos: '))

hora = seg // 3600
minutos = seg % 3600 // 60
segundos = seg % 60

print(f'{hora} horas(s), {minutos} minuto(s) e {segundos} segundos(s)')
