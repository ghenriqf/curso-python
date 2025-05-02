import time
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}') 
    if passo < 0:
        passo = passo * -1
    if fim > inicio:
        for numero in range(inicio, fim+1, passo):
            print(numero,end=' ',flush=True)
            time.sleep(0.2)
    else: 
        for numero in range(inicio, fim-1, passo - (passo*2)):
            print(numero,end=' ', flush=True)
            time.sleep(0.2)
    print('FIM!')    
inicio = int(input('Início: '))
fim = int(input('fim: '))
passo = int(input('Passo: ')) 
contador(inicio, fim, passo)
