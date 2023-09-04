import os
os.system('cls')

palindromo = input('Digite uma string que é um palíndromo: ')
inverso = palindromo[::-1]
if palindromo == inverso:
    print('A palavra inserida É um palíndromo.')

else:
    print('A palavra inserida NÃO é um palíndromo.')