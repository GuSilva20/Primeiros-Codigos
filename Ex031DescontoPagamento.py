produto = str(input("Nome do Produto: ")).strip()
preco = float(input("Preço do Produto? R$"))
print("Modos de Pagameento:")
print('[0] - Dinheiro: 10% de Desconto')
print('[1] - Cheque: 10% de Desconto.')
print('[2] - Cartão: 5% de Desconto.')
print('[3] - 2x no Cartão: Sem Desconto')
print('[4] - 3x ou mais no cartão: 20% de juros\n')

pag = int(input("Modo de Pagamento: "))
print("Produto: {}".format(produto))

if pag == 0 or 1:
    print("Desconto: 10%")
    des = preco - ((preco * 10) / 100)
elif pag == 2:
    print('Desconto: 5%')
    des = preco - ((preco * 5) / 100)
elif pag == 3:
    print("Sem Desconto! ")
    des = preco
elif pag == 4:
    print("Juros de 20%")
    des = preco + ((preco * 20) / 100)
else:
    print("Juros de 20%")
    des = preco + ((preco * 20) / 100)

print("Preço do produto: R${:.2f}".format(des))
