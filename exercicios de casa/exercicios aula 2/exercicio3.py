cidade = input('Qual a cidade que voce deseja ir: ')
distancia = float(input(f'Qual a distancia em km que voce vai percorrer para chegar ate a cidade de {cidade}: '))
tempo = int(input(f'Quanto tempo que ele percorreu em horas para chegar ate a cidade de {cidade}: '))

vm = distancia/tempo

print(f'A distancia percorrida para {cidade} é de {distancia} tudo isso percorrido em {tempo} horas, em uma velocidade media de {vm} km/h.')
