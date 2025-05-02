print('\033[0;32m-=\033[m'*20)
print('\033[0;32mAnalisador de Triângulos\033[m')
print('\033[0;32m-=\033[m'*20)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

maior = seg1
if seg2 > seg1 and seg2 > seg3:
    maior = seg2
if seg3 > seg2 and seg3 > seg1:
    maior = seg3
menor = seg1
if seg2 < seg1 and seg2 < seg3:
    menor = seg2
if seg3 > seg2 and seg3 <=seg1:
    maior = seg3
medio = seg1
if seg2 > menor and seg2 < maior:
    medio = seg2
if seg3 > menor and seg3 < maior:
    medio = seg3
if menor + medio > maior:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:   
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
    

