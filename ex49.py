import time
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

opcao_selecionada = 0

while opcao_selecionada != 6:

    opcao_selecionada = int(input(''''OPÇÕES
[ 1 ] SOMAR
[ 2 ] MUTIPLICAR
[ 3 ] SUBITRAIR
[ 4 ] DIVIDIR   
[ 5 ] NOVOS VALORES
[ 6 ] SAIR DO PROGRAMA 
Digite a opção:  '''))
    
    if opcao_selecionada == 1:
        print(f'{primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}')
        
    elif opcao_selecionada == 2:
       print(f'{primeiro_valor} x {segundo_valor} = {primeiro_valor * segundo_valor}') 
       
    elif opcao_selecionada == 3:
        print(f'{primeiro_valor} - {segundo_valor} = {primeiro_valor - segundo_valor}')
        
    elif opcao_selecionada == 4:
        print(f'{primeiro_valor} ÷ {segundo_valor} = {primeiro_valor / segundo_valor}')
    else:
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))


    time.sleep(1)
    
        

