def fatorial(num, show=False):
    """
    CALCULA UM FATORIAL
    num = número inteiro 
    show=False: Recebe dois parametros True ou False, que determina se vai exibir todo o processo do fatorial ou não
    return: Retorna o fatorial do número

    """
    fat = 1
    for n in range(num, 0, -1):
        if show:
            if n > 1:
                print(f'{n}', end=' x ')
            else:
                print('1 = ', end='')
        fat *= n
    return fat
print(fatorial(5, show=True))
help(fatorial)