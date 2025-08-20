import random
numero = int(input('Digite um numero de 0 a 5:'))
lista = [0,1,2,3,4,5]
if numero == random.choice(lista):
    print('Você é um cagado!')
else:
    print('Você errou feio!')

