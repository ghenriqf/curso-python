
media_idade = 0
contagem_mulher = 0
idade_masculina = 0
idade_homem = 0 
nome_homem = ''

for c in range (1,5):

    print(f'----{c}ª PESSOA----- ')
    nome = str(input('Nome: ')).strip()                                                 
    idade = int(input('Idade: '))                                               
    sexo = str(input('Sexo [M\F]: ')).upper 
    media_idade += idade
          
    if sexo == 'F' and idade < 20:
        contagem_mulher += 1
    if sexo == 'M' and idade_homem < idade:
        idade_homem = idade
        nome_homem = nome
    
    
print('A media da idade do grupo é de {:.2f} anos'.format(media_idade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_homem,nome_homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contagem_mulher))



   

    