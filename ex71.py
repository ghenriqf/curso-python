lista = []
x = str(input('Digite uma expressão: '))
for v in x:
    if v == '(':
        lista.append(v)
    elif v == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(v)
            break
if len(lista) == 0:
    print('Esta expressão esta correta!')
else:
    print('Esta expressão esta errada!')