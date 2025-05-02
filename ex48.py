print('Gerador de Progressão Aritmética')
print('='*32)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contagem = 0


while contagem < 10:  
    print(primeiro_termo,end= ' → ')
    
    primeiro_termo += razao
    contagem += 1
    
print('FIM',end = ' ')
