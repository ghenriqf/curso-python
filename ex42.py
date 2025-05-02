frase = str(input('Digite um frase: ')).upper()

frase_dividida = frase.split()

frase_inversa = frase[::-1]

frase_unida = ''.join(frase_dividida)

frase_inversa_dividida = frase_inversa.split()

frase_inversa_dividida_unida = ''.join(frase_inversa_dividida)


print('O inverso de {} é {}'.format(frase_unida,frase_inversa_dividida_unida))

if  frase_unida == frase_inversa_dividida_unida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

