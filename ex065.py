tupla = ('CURSO','PYTHON','ESTUDAR')
for palavras in tupla:
    print(f'\nNa palavra {palavras} temos: ',end = '')
    for letra in palavras:
        if letra in 'AEIOU':
            print(letra,end = ' ')
