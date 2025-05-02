numero = int(input('Digite um número: '))

contagem = 0
for c in range (1,numero+1):
     
    if numero % c == 0:
        contagem += 1
        print(f'\033[0;32m{c}\033[m', end= ' ')
    else:
          print(f'\033[0;31m{c}\033[m', end= ' ')
    
if contagem >= 3:
     print('\nO número {} foi divisível {} vezes \nE por isso NÃO É PRIMO!'.format(numero,contagem))
else:
    print('O número {} foi divisível {} vezes \nE por isso É PRIMO!'.format(numero,contagem)) 
     