import datetime

ano_atual = datetime.datetime.now().year
ano_nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Clasificação: MIRIM')
elif idade < 14 and idade > 9:
    print('Clasificação: INFANTIL')
elif idade < 19 and idade > 14:
    print('Clasificação: JUNIOR')
elif idade <= 20 and idade:
    print('Clasificação: SÊNIOR')
else:
    print('Clasificação: MASTER')