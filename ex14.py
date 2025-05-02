nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
nomes = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomes[0], len(nomes[0])))


