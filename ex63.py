a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))

tupla = (a,b,c,d)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3+1)}')
else:
    print('O valor 3 não apareceu')

print('Os valores pares digitados foram',end = ' ')
for numero in tupla:
    if numero % 2 == 0:
        print(numero,end = ' ')