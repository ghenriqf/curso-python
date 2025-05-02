registros = dict()
registros['Nome'] = str(input('Nome: '))
registros['Idade'] = int(input('Ano de Nascimento: '))
registros['Idade'] = 2024 - registros['Idade'] 
registros['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if registros['ctps'] != 0:
    registros['Contratação'] = int(input('Ano de Contratação: ')) 
    registros['Salário'] = float(input('Salário: R$'))
    registros['Aposentadoria'] = (2024 - registros['Contratação']) + 35 + registros['Idade']
print('=-'*40)
for i in registros:
     print(f'- {i} tem o valor {registros[i]}')