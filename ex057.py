homens = maior = mulheres = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')
