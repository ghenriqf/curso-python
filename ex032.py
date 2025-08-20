nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5.0:
    print('O aluno está REPORVAD!')
elif media >= 5.0 and media < 6.9:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')