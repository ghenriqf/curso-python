tupla = ('Lapís',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00)

print('='*50)
print('LISTAGEM DE PRODUTOS'.center(50))
print('='*50)

for produto in range(0,len(tupla)):
    if produto % 2 == 0:
        print(f'{tupla[produto]:-<40}',end = '')
    else:
        print(f'R$ {tupla[produto]:.2f}')

print('='*50)
    
