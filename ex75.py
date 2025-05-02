lista = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
soma_pares = maior = 0
for i in range(0, len(lista)):
    lista[i] = int(input(f'Insira um valor para posição {lista[i]}'))
    if lista[i] % 2 ==0:
        soma_pares+=lista[i]
for i in range(0,len(lista)):
    print('[', lista[i], end =' ]')
    if i ==2 or i==5:
        print('\n', end= '')
    if i > 2 and i < 6:
        if maior < lista[i]:
            maior = lista[i]
soma_coluna = lista[2]+lista[5]+lista[8]
print(f'\nA soma dos valores parés é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior}')