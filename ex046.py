import random

numero_aleatorio = random.randint(0,10)
numero_tentativas = 1

print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

palpite = int(input('Qual é o seu palpite ?'))

while palpite != numero_aleatorio:
    numero_tentativas += 1
    if numero_aleatorio < palpite:
        palpite = int(input('Menos... Tente mais uma vez. '))
    else:
        palpite = int(input('Mais... Tente mais uma vez. '))

print(f'Acertou com {numero_tentativas} tentativa. Parabéns!')