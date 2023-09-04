

num = int(input("Digite um numero decimal: "))

binario = ""
while num > 0:
    r = num%2
    binario = str(r) + binario
    num = num // 2

print(binario)



#num%2
#num//2
