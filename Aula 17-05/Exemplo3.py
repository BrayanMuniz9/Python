def imc(p, h):
    return p / (h**2)

p = float(input('Qual seu peso em KG: '))
h = float(input('Qual sua altura em m: '))

result = imc(p, h)
print(f'{result:.2f}')
