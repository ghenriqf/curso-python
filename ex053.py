resposta = 'sS'
soma = contagem = numero_maior = numero_menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]')).upper()
    soma += numero
    contagem += 1
    if contagem == 1:
        numero_menor = numero_maior = numero
    else:
        if numero > numero_maior:
            numero_maior = numero
        if numero < numero_menor:
            numero_menor = numero

print('Você digitou {} número e a sua média foi {}'.format(contagem,soma/contagem))
print('O maior valor foi {} e o menor foi {}'.format(numero_maior,numero_menor))