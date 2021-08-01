num = int(input('Digite um Numero de 4 digitos: '))

''' Errado
un = num[3]
dez = num[2]
cent = num[1]
mil = num[0]
'''
# Gabarito -------------------------------
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
a = num // 10
print('Analisando o número: {}'.format(num))
print('Unidade : {}'.format(u))
print('Centena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
