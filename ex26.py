salario = int(input('Digite o seu salário para saber o seu aumento: '))

if salario > 1250:
    print('Você recebeu um aumento de 10%, seu salário ficou {:.2f}'.format(salario*0.10+salario))
else:
    print('Você recebeu um aumento de 15%, seu salário ficou {:.2f}'.format(salario*0.15+salario))