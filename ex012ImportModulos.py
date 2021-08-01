#immporta toda a bliblioteca

#import math
from math import sqrt,ceil,floor
import random

num = int(input('Digite um número: '))
raiz = sqrt(num)

#numero aleatorio
n1 = random.randint(1, 10)
print(n1)

print('A raiz de {} é igual a {}'.format(num,raiz))
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

#Arredonda para cima
#print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num,ceil(raiz)))

#arredonda para baixo
#print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))


