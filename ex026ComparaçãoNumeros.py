n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))

if n1 > n2:
    print("O PRIMEIRO valor é MAIOR".format(n1))
elif n1 < n2:
    print('O SEGUNDO valor é MAIOR'.format(n2))
else:
    print('Os DOIS valores são IGUAIS!!')
