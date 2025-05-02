def ficha(nome, gols):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato! '
nome = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
print(ficha(nome,gols))
