nome=input("Qual seu nome? ")
saldo=float(input(("Quanto dinheiro você tem?[R$] ")))
moeda=float(input("Valor do Cambio atual: "))

conversao =float(saldo / moeda)

print('Total Convertido: {}'.format(conversao))
#Gabarito
print('Com {}R$ você pode Comprar ${:.2f}'.format(saldo,conversao))
