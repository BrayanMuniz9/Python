import os
os.system('cls')

email = input('Entre com o seu e-mail: ')
dominio = email.split('@')[1]

print(f'O domínio do seu email é http://{dominio}')