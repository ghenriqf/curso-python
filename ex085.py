def escreva(txt):
    print(f'~{'~'*len(txt)}~')
    print(f'{txt}'.center(len(txt)+2))
    print(f'~{'~'*len(txt)}~')
txt = (str(input('Digite sua palavra: ')))
escreva(txt)