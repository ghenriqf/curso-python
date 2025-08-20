import random
import time
print('-'*20)
print('MEGA SENA'.center(20))
print('-'*20)
numeros = list()
jogos = list()
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for n in range (0,quantidade_jogos):
    cont = 0
    while True:
        numero_aleatorio = random.randint(1,60)
        if numero_aleatorio not in numeros:
            numeros.append(numero_aleatorio)
            cont+=1
        if cont ==6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
for q, j in enumerate(jogos):
    print(f'Jogo {q+1}: {j}')
    time.sleep(1)
print('-=-=-=-=-=- < BOA SORTE! > -=-=-=-=-=-')