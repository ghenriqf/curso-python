import time

numero = int(input('Digite um numero inteiro: '))
time.sleep(1)
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {} '.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')