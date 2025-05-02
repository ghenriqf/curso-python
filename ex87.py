import time
def maior(*num):
    maior = 0
    print('=-'*30)
    print('Os números escolhidos foram...')
    for n in num:
        time.sleep(0.5)
        print(n, end=' ', flush=True)
        if n > maior:
            maior = n
    print(f'Foram informados {len(num)} ao todo. \nO maior valor integrado foi {maior}')
maior(2,4,1,23,5,2,1)
maior(3,5,1,2,7,2,3,4)

