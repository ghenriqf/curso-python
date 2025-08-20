dis = float(input('Qual é a distância da sua viagem: '))
if dis >= 200:
    print('Sua passagem vai custar {:.2f}R$'.format(dis*0.45))
else:
    print('Sua passagem vai custar {:.2f}R$'.format(dis*0.50))