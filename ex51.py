print('='*50)
print('{}'.format('Sequência de Fibonacci'.center(50)))
print('='*50)
numero = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} - {}'.format(t1,t2),end=' - ')
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print('{}'.format(t3),end=' - ')
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')





    
   