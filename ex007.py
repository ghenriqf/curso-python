a = float(input('Qual é a altura da parede? '))
l = float(input('Qual é a largura da parede? '))
print(' Sua parede tem dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m2\n Para pintar a sua parede, você precisará de {:.2f} litros tinta '.format(a,l,a*l, a*l/2))