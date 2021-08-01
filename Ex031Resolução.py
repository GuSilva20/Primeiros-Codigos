print('{:=^40}'.format(" LOJAS GUGOD "))
preco = float(input("Preço da Compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista Dinheiro/Cheque:
[ 2 ] a vista cartão:
[ 3 ] 2x no cartão:
[ 4 ] 3x ou mais no cartâo''')
opcao = int(input("Qual é a opção? "))

if opcao == 1 :
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra seá parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4 :
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDADE de pagamento. Tente novamente!.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
