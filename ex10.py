import math
catetooposto = float(input('Digite o cateto oposto: '))
catetoadjacente = float(input('Digite o adjacente : '))
resultado = math.hypot(catetooposto, catetoadjacente)
print('A hipotenusa vai medir: {:.2f}'.format(resultado))