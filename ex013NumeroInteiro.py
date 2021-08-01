'''Exercicio de Aredondamento de numero inteiro / e pitagoras '''
'''Aredondamento de números '''

''' import math'''
from math import trunc

n1 = float(input("Digite um número: "))

# Errado-------Esta arredondado para o mais proximo ------------------------------
print("{:.0f}".format(n1))
print('O valor digitado foi {}, o número inteiro é: {:.0f}'.format(n1, n1))
# Errado -----------------------------------------------------------------------

# gabarito------------------------------------------------------------------------
'''print('O valor Digitado foi {} e a sua porção inteira é {}'.format(n1,math.trunc(n1)))'''
print('O valor digitado foi {} e a sua porção inteira é {}:'.format(n1, trunc(n1)))
print('o valor digitado foi {} e a sua porção inteir é {}:'.format(n1, int(n1)))
# gabarito------------------------------------------------------------------------


'''Exercicio de pitagoras'''

print('Triango Pitagoras')
print('--' * 10)
print('a2 = b2 + c2')
print('Digite os valores: ')
co = float(input('Cateto Oposto[b]: '))
ca = float(input('cateto Adjacente[c]: '))

# Respota errada -------------------------------------
print('Hipotenusa vai medir {}'.format((co * 2) + (ca * 2)))


#Gabarito -----------------------------------------------
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai merid {:.2f}'.format(hi))