nu1 = int(input('Digite um numero: '))
nu2 = int(input('Digite outro numero: '))
nu3 = int(input('Digite outro numero: '))

if nu1 < nu2 and nu1 < nu3:
    menor = nu1
if nu2 < nu1 and nu2 < nu3:
    menor = nu2
if nu3 < nu1 and nu3 < nu2:
    menor = nu3
if nu1 > nu2 and nu1 > nu3:
    maior = nu1
if nu2 > nu1 and nu2 > nu3:
    maior = nu2
if nu3 > nu1 and nu3 > nu2:
    maior = nu3
print ('O numero maior é o {} e o menor é o {}'.format(maior,menor))



