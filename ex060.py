numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')

while True:
    escolha = int(input('Escolha um número de 0 a 20: '))
    if  0 <= escolha <=20:
        break
    print('Tente novamente...') 
    
print(f'Você digitou o número {numeros[escolha]}')
