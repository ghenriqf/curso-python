numeros = []
while True:
    valor = int(input('Digite um valor:'))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Valor não adicionado...')
    escolha = str(input('Quer continuar? [S/N]')).upper()
    if escolha == 'N':
        break
numeros.sort()
print(f'Os valores digitado foram: {numeros}')

