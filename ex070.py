lista = []
lista_par = []
lista_impar = []
while True:
   num = int(input('Digite um número: '))
   lista.append(num)
   if num%2==0:
      lista_par.append(num)
   else:
      lista_impar.append(num)
   escolha = str(input('Quer continuar?'))
   if escolha in 'Nn':
      break
print(f'A lista completa é {lista}')       
print(f'A lista de pares é {lista_par}')       
print(f'A lista de ímpares é {lista_impar}')