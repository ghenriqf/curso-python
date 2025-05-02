import math
ang = int(input('Digite um valor de um angulo: '))
ang2 = math.radians(ang)
sen = math.sin(ang2)
cos = math.cos(ang2)
tan = math.tan(ang2)
print('O seno do seu angulo é:{:.2f}'.format(sen))
print('O coseno do seu angulo é:{:.2f}'.format(cos))
print('A tangente do seu angulo é:{:.2f}'.format(tan))  
