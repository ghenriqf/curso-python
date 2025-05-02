cadastros = list
media_idade = list()
while True:
    registro = dict()
    registro['Nome'] = str(input('Nome: '))
    registro['Sexo'] = str(input('Sexo: [M/F] ')).upper()
    while registro['Sexo'] not in 'FM':
        del(registro['Sexo'])
        print('ERRO! Por Favor, digite apenas M ou F.')
        registro['Sexo'] = str(input('Sexo: [M/F] ')).upper()
    registro['Idade'] = int(input('Idade: '))
    media_idade.append(registro['Idade'])
    continuar = str(input('Quer continuar: [S/N]')).upper()
    while continuar not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        continuar = str(input('Quer continuar: [S/N]')).upper()
    cadastros.append(registro)
    if continuar in 'N':
        break
media = sum(media_idade) / len(cadastros)
print('=-'*30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A média de idades é {media:.2f} anos')
print(f'C) As mulheres cadastradas foram:', end=' ')
for c in cadastros:
    if c['Sexo'] == 'F':
        print(c, end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for i in cadastros:
    if i['Idade'] > media_idade:
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
print('>>ENCERRADO<<')
            
    
