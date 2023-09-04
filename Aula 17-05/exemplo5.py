import trigonometria

catO = float(input('Qual é o cateto oposto? '))
catA = float(input('Qual é o cateto adjascente? '))

print(f'Seno = {trigonometria.seno(catO, catA)}')
print(f'Cosseno = {trigonometria.cosseno(catO, catA)}')
print(f'Tangente = {trigonometria.tang(catO, catA)}')