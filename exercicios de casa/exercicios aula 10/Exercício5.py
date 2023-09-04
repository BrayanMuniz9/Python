import os
os.system('cls')

cont = 0
print('Se divirta jogando FizzBuzz!')
while cont == 0:
    num = int(input('Digite um número inteiro de 1 - 50: '))
    if num < 1 or num > 50:
        print('Número inválido.')

    elif num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
        ans = input('Jogar novamente? (s/n): ')
        if ans.lower() != 's':
            cont += 1

    elif num%3 == 0:
        print('Fizz')
        ans = input('Jogar novamente?(s/n): ')
        if ans.lower() != 's':
            cont += 1

    elif num%5 == 0:
        print('Buzz')
        ans = input('Jogar novamente?(s/n): ')
        if ans.lower() != 's':
            cont += 1

    elif num%3 != 0 and num%5 != 0:
        print(num)
        ans = input('Jogar novamente?(s/n): ')
        if ans.lower() != 's':
            cont += 1