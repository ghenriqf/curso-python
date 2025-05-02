valor_casa = int(input('Valor da casa: R$'))
salario_comprador = int(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento: '))
prestacao = valor_casa/(anos*12)

if prestacao >= 0.30 * salario_comprador:
    print('Para pagar essa casa de {} em {} anos a prestação será de {:.2f} \nEmpréstimo NEGADO!'.format(valor_casa,anos,prestacao))
else:
    print('Para pagar essa casa de {} em {} anos a prestação será de {:.2f} \nEmpréstimo CONCEDIDO!'.format(valor_casa,anos,prestacao))