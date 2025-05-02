import random
import time
numeros = list()
def sorteio():
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(0, 5):
        time.sleep(0.5)
        numeros.append(random.randint(1,10))
        print(numeros[c], end=' ', flush=True)
    print('PRONTO!')
def somapar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')
sorteio()
somapar()

    
