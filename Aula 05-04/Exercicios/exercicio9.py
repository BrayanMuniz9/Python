import os
os.system('cls')

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

print('[1] Média\n[2] Diferença maior-menor\n[3] Produto\n[4] Divisão')

opcao = int(input('Digite uma opção: '))

if opcao == 1:
    media = (num1 + num2) / 2
    print(f'Media = {media}')
elif opcao == 2:
    if num1>num2:
        diff = num1 - num2
        print(f'Diferença = {diff}')
    else:
        print(f'Diferença {num2 - num1}')
elif opcao == 3:
    produto = (num1 * num2)
    print(f'Produto = {produto}')
elif opcao == 4:
    if num1 > 0 and num2 > 0:
        divisao = num1 / num2
        print(f'Divisão = {divisao}')
    else:
        print('Impossivel dividir por zero!!!')
else:
    print(f'Opção invalida!')
