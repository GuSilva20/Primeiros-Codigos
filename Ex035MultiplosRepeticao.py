s = 0
for c in range (1, 501):
    if c % 3 == 0:
        print('Número: {}'.format(c))
        s += c
        print('Soma: {} '.format(s))
print("Programa Finalizado!")