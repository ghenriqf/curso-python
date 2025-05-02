print('='*40)
print('\033[0;34mSUPER MERCADO FREITAS\033[m'.center(50))
print('='*40)

preco_compras = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista no dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao_selecionada = int(input('Qual é a opção? '))

if opcao_selecionada == 1:
    desconto = preco_compras - (preco_compras*0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_compras,desconto))

elif opcao_selecionada == 2:
    desconto = preco_compras - (preco_compras*0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_compras,desconto))

elif opcao_selecionada == 3:
   valor_parcela = preco_compras/2
   print('Sua compra será parcelada em 2x de {:.2f}'.format(valor_parcela))

elif opcao_selecionada == 4:
        quantidade_parcelas = int(input(('Quantas parcelas? ')))
        if quantidade_parcelas == 2:
             print('Sua compra será parcelada em 2x de {:.2f}'.format(preco_compras/2))
        elif quantidade_parcelas >= 3:

            preco_parcelado = preco_compras + (preco_compras * 0.20)
            valor_parcela = preco_parcelado / quantidade_parcelas

            print('Sua compra será parcelada em {}x de {:.2f} \nSua compra de R${:.2f} vai custar R${:.2f} no final'.format(quantidade_parcelas,valor_parcela,preco_compras,preco_parcelado))
          
else:
    print('Opção de pagamento inválida.')
