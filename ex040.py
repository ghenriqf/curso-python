print('='*35)
print('{}'.format('10 TERMOS DE UMA PA'.center(35)))
print('='*35)

termo_1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


for c in range (0,10):
    print(termo_1)
    termo_1 = termo_1 + razao

print('ACABOU')