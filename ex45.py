sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo =  str(input('Dados inválidos. Por favor, informe novamente:')).strip().upper()[0] 
if sexo in 'Mm':
    m = 'Masculino'
elif sexo in 'Ff':
    m = 'Feminino'
print(f'Sexo {m} registrado com sucesso!')
