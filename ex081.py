registro = dict()
gols = list()
registro['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {registro["Nome"]} jogou? '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
registro['Gols'] = gols
registro['Total'] = sum(gols)
print('-=' * 30)
print(registro)
print('-=' * 30)
for k, v in registro.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {registro["Nome"]} jogou {partidas} partidas.')
for c, i in enumerate(gols):
    print(f'=> Na partida {c + 1}, fez {i} gols.')
print(f'Foi um total de {registro["Total"]} gols!')

