import os
os.system('cls')

print('Pagamento de contas')
agua = float(input('Valor da conta de água: R$ '))
luz = float(input('Valor da conta de energia: R$ '))
internet = float(input('Valor da conte de internet: R$ '))
salario = float(input('Qual é o seu atual salario? R$ '))

contas = agua + luz + internet

if salario > contas:
    print(f'Suas contas deu no total de R$ {contas}, voce vai conseguir pagar e ainda te sobrará R$ {salario - contas}.')
else:
    print(f'Salario insuficiente, ainda falta R$ {contas - salario} para pagar as contas.')
