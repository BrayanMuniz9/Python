import os, math
os.system('cls')
cont = 0

while cont == 0:

  nome = input('Digite o nome de usuário: ')
  print(f'Olá {nome}.')

  print(f'Digite 1 para: Conversão da base decimal para as bases binário, hexadecimal e octadecimal.')
  print(f'Digite 2 para: Conversão das bases binário, hexadecimal e octadecimal para a base decimal.')
  print(f'Digite "Esc" durante o menu para sair.')

  menu = input('Insira uma opção: ')

  if menu == '1':
    print('Digite 1 para: Converter da base decimal para a base binário: ')
    print('Digite 2 para: Converter da base decimal para a base hexadecimal: ')
    print('Digite 3 para: Converter da base decimal para a base octadecimal: ')

    opcao1 = input('Insira uma opção: ')

    if opcao1 == '1':
        binario = ""
        dec = int(input('Digite um número para conversão: '))
        while dec > 0:
            r = dec%2
            binario = str(r) + binario
            dec = dec //2
            cont += 1
        print(f'Binário = {binario}')
        
    elif opcao1 == '2':
        dec = int(input('Digite um número para conversão: '))
        hexa = ""
        while dec > 0:
          r = dec%16
          dec = dec // 16
          if r < 10:
            hexa = str(r) + hexa
        else:
            hexa = chr(ord('A') + r - 10) + hexa
            cont += 1
        print(f'Hexadecimal = {hexa}')
        
    elif opcao1 == '3':
        dec = int(input('Digite um número para conversão: '))
        octal = ""
        while dec > 0:
          r = dec%8
          dec = dec // 8
          octal = str(r) + octal
          cont =+1
        print(f'Octodecimal = {octal}')
        
    elif opcao1.lower() == 'esc':
      break
  
  elif menu == '2':
    print('Digite 1 para: Converter da base binário para a base decimal: ')
    print('Digite 2 para: Converter da base hexadecimal para a base decimal: ')
    print('Digite 3 para: Converter da base octadecimal para a base decimal: ')
    
    opcao2 = input('Insira uma opcão: ')
    
    if opcao2 == '1':
      num = input('Digite um número para conversão: ')
      n = len(num)-1
      dec1 = 0
      for bin in num:
        dec1 = dec1 + int(bin)*2**n
        n = n - 1
        cont =+1
      print(f'Decimal = {dec1}')

    elif opcao2 == '2':
      num = input('Digite um número para conversão: ')
      dec = int(num, 16)
      cont =+1
      print(f'Decimal = {dec}')
      
    elif opcao2 == '3':
      num = input('Digite um número para conversão: ')
      n = len(num)-1
      octa = 0
      for b in num:
        octa = octa + int(b)*8**n
        n = n - 1
        cont =+1
      print(f'Decimal = {octa}')
      
    elif opcao2.lower() == 'esc':
      break
    
  elif menu.lower() == 'esc':
    break