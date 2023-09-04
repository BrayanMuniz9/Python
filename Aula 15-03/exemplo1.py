num = int(input('Digite um numero de tres algarismos: '))

d1 = num//100
d2 = num%100//10
d3 = num%10

print(f'{d3}{d2}{d1}')
