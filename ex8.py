dia = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km foram rodados? '))
precod = dia*60
precokm = km*0.15
print('Total a pagar é de {:.2f}R$'.format(precod+precokm))
