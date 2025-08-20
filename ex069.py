numeros = []
while True:
    numeros.append(int(input('Digite um valor:')))

    escolha = str(input('Quer continuar? '))
    if escolha in 'Nn':
        break
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrecente são {numeros}')

if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')