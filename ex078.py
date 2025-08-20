aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'A Média de {aluno["Nome"]}: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
for k, i in aluno.items():
    print(f'{k} é igual a {i}')