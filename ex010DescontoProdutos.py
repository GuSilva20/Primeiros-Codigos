Produto = input('Produto: ')
Preco=float(input("Preço do produto em R$: ".format(Produto)))
Desconto = float(input("Desconto [%]: "))

desc = (Preco * Desconto)/100
PrecoDesconto = Preco - desc

print('A {} com desconto de {}% saira por {:.2f}R$'.format(Produto, Desconto, PrecoDesconto))

#Gabarito
print("com desconto o produto saira por:{:.2f}RS ".format(Preco - (Preco * Desconto / 100)))
