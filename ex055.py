while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    print('-'*30)
    for s in range (0,11):
        
        print(f'{numero} X {s} = {numero*s}')
    print('-'*30)
    if numero < 0:
        break
print('PROGRAMA ENCERRANDO...')
