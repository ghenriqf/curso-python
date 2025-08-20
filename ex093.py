def boletim(*notas, sit=False):
    """
    -> Função para anlisar diversas e situações.
            nota: Notas do aluno(aceita diversas notas).
            sit: Valor opicional, idicando se deve ou não adicionar a situação.
            return: Retorna o dicionario com as informações do aluno.
    """
    nota = dict()
    maior = menor = 0
    for n in notas:
        if n > maior:
            maior = n
        if menor == 0:
            menor = n
        if n < menor:
            menor = n
    nota['total'] = len(notas)
    nota['maior'] = maior
    nota['menor'] = menor
    nota['média'] = sum(notas) / len(notas)
    media = nota['média']
    if sit:
        if media < 6:
            nota['situação'] = 'Ruim'
        elif 6 <= media < 7:
            nota['situação'] = 'Razoável'
        elif media > 6.9:
            nota['situação'] = 'Bom' 
    return nota
resp = boletim(7.0, 8.0, 4, 8, sit=True)
print(resp)
help(boletim)