lista = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
for i in range(0, len(lista)):
    lista[i] = int(input(f'Insira um valor para posição {lista[i]}:'))
for i in range(0,len(lista)):
    print('[', lista[i], end =' ]')
    if i ==2 or i==5:
        print('\n', end= '')