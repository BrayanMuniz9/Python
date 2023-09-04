import os
os.system('cls')

carn = 0

while True:
    resp = input('Já dormiu (s/n) ')
    if resp in "sS":
        break
    carn += 1

print(carn)
