def leiaint(txt):
    while True:
        try:
            inteiro = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO, número inteiro inválido!')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não colocar este espaço!')
            return 0
        else:
            return inteiro

def leiareal(txt):
    while True:
        try:
            real = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO, número real inválido!')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não colocar este espaço!')
            return 0
        else:
            return real
            

inteiro = leiaint('Digite um número inteiro: ')
real = leiareal('Digite um número real: ')
print(f'O número inteiro foi {inteiro} e o real foi {real}')