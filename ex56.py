import random
print('='*30)
print('JOGO DO PAR OU ÍMPAR')
print('='*30)

cont = 0

while True:
    numero_computador = random.randint(1,10)

    escolha = str(input('Escolha entre par ou ímpar: '))
    
    escolha_numero = int(input('Escolha um número de 1 a 10: '))
    soma = escolha_numero + numero_computador

    if  escolha == 'par' and soma%2 > 0 or escolha == 'impar'and soma%2 == 0:
        print(f'Você perdeu!! O computador jogou {numero_computador} e você {escolha_numero} a soma da {numero_computador+escolha_numero}')
        break
    else:
        print('VENCEU!!')
        cont += 1
    
print(f'Você ganhou {cont} vezes seguidas')
    

    
    

    

