soma = 0
cont = 0
for c in range (3,501):
    if c % 2 == 1 and c % 3 == 0:
       cont = cont + 1
       soma = soma + c
print('A soma te todos os {} valores é {} '.format(cont,soma))
    
