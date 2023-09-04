import os
os.system('cls')

numeros = []
positivos = 0
negativos = 0

while True:
    valor = float(input("Digite um valor (ou 0 para sair): "))
    if valor == 0:
        break
    numeros.append(valor)
    if valor > 0:
        positivos += 1
    else:
        negativos += 1

if len(numeros) > 0:
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    print("Foram digitados", positivos, "valores positivos e", negativos, "valores negativos.")
    print("O menor valor é:", menor)
else:
    print("Nenhum valor foi digitado.")