import os
os.system('cls')

tc = float(input('Digite uma temperatura em Celsius: '))

tf = 1.8 * tc + 32
tk = tc + 273

print(f'A temperatura {tc:.2f}°C \n{tf:.2f}°F em Fahrenheit \n{tk:.2f}°K em Kelvin.')
