ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('O ano de {} é BIXSSESTO'.format(ano))
else:
    print('O ano de {} não é BIXSSESTO'.format(ano))
