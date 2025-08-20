import random
import time
jogadores = dict()
print(' VALORES SORTEADOS ')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = random.randint(1, 6)
    print(f'Jogador{c} tirou {jogadores[f'jogador{c}']}')
    time.sleep(1)
print('='*40)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(sorted(jogadores, key= jogadores.get, reverse=True)):
    print(f'{i+1}° lugar: {v} tirou {jogadores[v]}')
    time.sleep(1)