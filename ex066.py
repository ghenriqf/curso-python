valores = []
maior = menor = 0

for num in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {num}: ')))
    if num == 0:
        maior = menor = valores[num]
    else:
        if valores[num] < menor:
            menor = valores[num]
        if valores[num] > maior:
            maior = valores[num]
print(f'\nOs valores digitados foram {valores}')

print(f'O maior valor digitado foi {maior} na posição: ', end = '' )
for pos, val in enumerate(valores):
    if val == maior:
        print(f'{pos}',end=' ')
print(f'\nO menor valor digitado foi o {menor} na posição: ', end = '')
for pos, val in enumerate(valores):
    if val == menor:
        print(f'{pos}', end =' ')