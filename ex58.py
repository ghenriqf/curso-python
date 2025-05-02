compra = mil = menor = cont = 0
barato = ' '
while True:
    cont += 1
    continuar = ' '
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    
    compra += preço
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    if continuar == 'N':    
        break

print(f'O toal da compra foi R${compra:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')



