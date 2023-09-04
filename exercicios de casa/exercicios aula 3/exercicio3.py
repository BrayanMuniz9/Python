import os
os.system('cls')

print('Digite a sua idade em anos, meses e dias.')
anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

anos1 = anos * 365
meses1 = meses * 30
idadedias = anos1 + meses1 + dias

print(f'Logo você tem {idadedias} dias de vida. ')
