n1 = int(input('Digite um número: '))
print(type(n1))
ant = n1 - 1
suc = n1 + 1
dobro = n1 * 2
triplo = n1 * 3
Raiz = n1**(1/2)

#resposta
print('Antecessor {} \nSucessor {}'.format(ant,suc))
print('Dobro: {} \nTriplo: {}'.format(dobro,triplo))
print('Raiz Quadrada {}'.format(Raiz))


#Gabarito
print("Analisando o número: {} \nAntecessor: {} \nSucessor: {}".format(n1,n1-1,n1+1))
print('Analisando o número: {}  \nDobro: {}, \nTripo: {} \nRaizQuadrada: {:.2f}'.format(n1,n1*2,n1*3,Raiz))


