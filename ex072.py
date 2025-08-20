pessoas = []
dados = []
maior = menor = 0
nome_maior = []
nome_menor = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar?'))
    if escolha in 'Nn':
        break

for p in pessoas:
    if maior == 0:
        maior = p[1]
        nome_maior.append(p[0])
        menor = p[1]  
        nome_menor.append(p[0])
    else:
        if p[1] > maior:
            maior = p[1]
            nome_maior.clear()
            nome_maior.append(p[0])
        elif p[1] == maior:
            nome_maior.append(p[0])

        if p[1] < menor:
            menor = p[1]
            nome_menor.clear()
            nome_menor.append(p[0])
        elif p[1] == menor:
            nome_menor.append(p[0])
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}, peso de {nome_maior} ')
print(f'O menor peso foi de {menor}, peso de {nome_menor}')