soma = 0
contagem = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um número (999 para parar): '))
    if numero < 999:
        soma += numero
    contagem += 1

print('Você digitou {} números e a soma entre eles foi {}'.format(contagem,soma))
