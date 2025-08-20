import datetime
ano_atual = datetime.datetime.now().year


contagem_maior = 0
contagem_menor = 0

for c in range (1,8):
    ano = int(input(f'Em que ano a {c}ª nasceu?'))
    idade = ano_atual - ano
    if idade >= 18:
        contagem_maior += 1
    else:
        contagem_menor += 1
print(f'Ao todo tivemos {contagem_maior} pessoas maiores de idade \nE também tivemos {contagem_menor} pessoas menores de idade')
