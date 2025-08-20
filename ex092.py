def inteiro(n):
    while True:
        na = input(n)
        if na.isnumeric():
            return na
        print('ERRO! Digite um número válido')        
n = inteiro('Digite um número: ')
print(f'Você acabou de digitar o número {n}')