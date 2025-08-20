jogadores = list()
while True:
    gols = list() 
    registro = dict()
    registro["nome"] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {registro["nome"]} jogou? '))
    for c in range(1, partidas+1):
            gols.append(int(input(f'Quantos gols na {c} partida? ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    registro['gols'] = gols
    jogadores.append(registro)
    if continuar in 'N':
          break
print('=-'*30)
print(f'{'cod':<5}{'Jogador':<20}{'Gols':>1}{'Total':>14}')
print('='*40)
for n, v in enumerate(jogadores):
      print(f'{n+1:<5}{jogadores[n]["nome"]:<20}{str(jogadores[n]["gols"]):>2}{sum(jogadores[n]["gols"]):>12}')
print('='*40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
          break
    elif dados <= 0 or dados > len(jogadores):
          print('JOGADOR NÃO ENCONTRADO TENTE NOVAMENTE.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados-1]["nome"]}')
        for n in range(0, len(jogadores[dados-1]["gols"])):
              print(f'No jogo {n} ele fez {jogadores[dados-1]["gols"][n]}')  
    



    
