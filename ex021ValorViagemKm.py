km = float(input('Digite a distancia da viagem: '))

if km <= 200:
    print('O valor da viagem ficara: {:.2f} Reais'.format(km * 0.50))
else:
    print('O valor da viagem ficara: {:.2f} Reais'.format(km * 0.45))


#Gabarito
print("Você está preste a iniciar a viagem!")
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print("O Preço da sua passagem será de: R${:.2f}".format(preço))




