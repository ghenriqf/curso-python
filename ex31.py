import datetime

ano_atual = datetime.datetime.now().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} em {ano_atual}. ')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    print('Você já deveria ter se alistado há {}'.format(idade - 18))
else:
    print('Ainda faltam {} anos para o alistamento'.format(idade - 18))
