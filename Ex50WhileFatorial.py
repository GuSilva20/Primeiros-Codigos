""" Rolução 1 - modulo math
from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print('O fatorial de {} e {}'.format(n, f))"""

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print("Calculando {}! = ".format(n), end='')
# while c > 0:
#    print('{}'.format(c), end="")
#    print(' x ' if c > 1 else ' = ', end='')
#    f *=  c
#    c -= 1
# print('{}'.format(f))
# print("O Fatorial de {} e {}".format(n, f, f))
# c = inicio da contagem
# b = final da contagem
# c = Passo da contagem -1 conta de traz pra frente, 1 conta de frento...
#               a,b,c
for c in range(c, 0, -1):
    print('{}'.format(c), end="")
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
