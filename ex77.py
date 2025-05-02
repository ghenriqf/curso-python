dados = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    dados.append([nome,[nota1,nota2],media])
    escolha = str(input('Quer continuar?[S/N]'))
    if escolha in 'Nn':
        break
print('-='*20)
print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*40)
for i,a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    num = int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if num == 999:
        break
    print(f'Notas de {dados[num][0]} são {dados[num][1]}')
