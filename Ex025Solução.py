casa = float(input("Valos da casa: R$"))
salario = float(input("Saálrio do Comprador: R$"))
anos = int(input("Quantos anos de financimanto? "))
prestacao = casa / (anos * 12)
minimo = ((salario * 30) / 100)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print("a prestação será de R${:.2f}".format(prestacao))
#print("comparando tem que pagar {:.2f} e o minimo é {}".format(prestacao,minimo))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
