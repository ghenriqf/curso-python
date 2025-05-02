import time

print('\033[0;32m-=\033[m'*20)
print('\033[0;32mRADAR\033[m'.center(50))
print('\033[0;32m-=\033[m'*20)
time.sleep(2)

velocidade = float(input('Qual é a velocidade do carro? '))

if velocidade >= 80:
    print('\033[0;31m MULTADO... Dirige certo po! Sua multa vai custar {} reais \033[m'.format((velocidade-80)*7))
else:
    print('\033[0;32m PASSOU... Boa viajem! \033[m')