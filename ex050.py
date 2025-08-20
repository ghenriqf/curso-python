print('Gerador de Progressão Aritmética')
print('='*32)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Qual é a razão: '))
termo = primeiro_termo
contagem = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while contagem <= total:
        print(termo, end = ' → ')
        contagem += 1
        termo = termo + razao
    print('PAUSA') 

    mais = int(input('Quantos termos a mais: '))

print('fim')   