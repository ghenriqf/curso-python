frase = str(input('Digite uma frase: ')).strip()
frase.lower
print('Quantas vezes aparece a letra A: {}'.format(frase.count('a')))
print('Em que posição o A aparece pela primeira vez: {}'.format(frase.find('a')+1))
print('Em que posição o A aparece pela última vez: {}'.format(frase.rfind('a')+1))