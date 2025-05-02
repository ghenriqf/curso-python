numero = int(input('Digite um número para \ncalcular seu Fatorial: '))

fatorial = 1
while numero > 0:
    fatorial *= numero
    
    if numero != 1:
        print(f'{numero}', end=' X ')
    else:
        print('1 = ',end='')
    numero -= 1

print(fatorial)

    
    



   
   


